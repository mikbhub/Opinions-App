from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormView

from dispatch_to_support.dispatcher import CustomerSupportDispatcher
from dispatch_to_support.forms import ResponseForm
from dispatch_to_support.models import Response, SupportTicket


dispatcher = CustomerSupportDispatcher()
# Create your views here.
class QueueView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = [
        'dispatch_to_support.change_supportticket'
    ]

    raise_exception = False

    def get(self, request):
        ctx = {
            'open_tickets': self.request.user.supportticket_set.filter(status=0)  # get open tickets
        }
        return render(request, 'dispatch_to_support/get_case.html', ctx)

    def post(self, request):
        sentiment, data = dispatcher.give_next_customer_case(give_to=self.request.user)
        feedback = data["feedback"]
        support_ticket = data["support_ticket"]
        context = {
            'queue': dispatcher.queue.empty(),
            'sentiment': sentiment,
            'feedback': feedback,
        }
        try:
            return redirect('dispatch_to_support:ticket-update', pk=support_ticket.pk)
        except AttributeError:
            return render(request, 'dispatch_to_support/queue.html', context)


class SupportTicketDetailView(LoginRequiredMixin, DetailView):
    model = SupportTicket
    template_name = "dispatch_to_support/support_ticket_detail.html"


class SupportTicketUpdateView(PermissionRequiredMixin, UpdateView):
    
    permission_required = [
        'dispatch_to_support.change_supportticket'
    ]
    raise_exception = True
    
    model = SupportTicket

    fields = [

    ]
    template_name = "dispatch_to_support/support_ticket_update.html"
    success_url = reverse_lazy('dispatch_to_support:queue')

    def form_valid(self, form):
        form.instance.support_person = self.request.user
        form.instance.status = 1  # Closed
        form.instance.closed = timezone.localtime()
        return super(SupportTicketUpdateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SupportTicketUpdateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        customer = self.object.feedback.customer
        context['customer_past_ticket_list'] = SupportTicket.objects.filter(
            feedback__customer=customer, 
            status=1
            )
        print(context['customer_past_ticket_list'])
        return context


class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        ctx = {
            'open_tickets': self.request.user.supportticket_set.filter(status=0)  # get open tickets
        }
        return render(request, 'dispatch_to_support/dashboard.html', ctx)


class ResponseCreateView(FormView):
    template_name = "dispatch_to_support/response_form.html"
    form_class = ResponseForm
    success_url= reverse_lazy('dispatch_to_support:dashboard')

    def post(self, request, ticket_pk, *args, **kwargs):
        form = ResponseForm(data=request.POST)
        form.instance.support_person = self.request.user
        form.instance.support_ticket = SupportTicket.objects.get(pk=ticket_pk)
        form.save()
        return redirect('dispatch_to_support:ticket-update', pk=ticket_pk)


class ResponseDetailView(DetailView):
    model = Response
    template_name = "dispatch_to_support/response_detail.html"
