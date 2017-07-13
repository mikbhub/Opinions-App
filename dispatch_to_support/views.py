from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from dispatch_to_support.dispatcher import CustomerSupportDispatcher
from dispatch_to_support.models import SupportTicket
from django.utils import timezone

# some debug
def sample_gen():
    i = 1
    while i:
        yield i
        i += 1

gen = sample_gen()
dispatcher = CustomerSupportDispatcher()
# Create your views here.
class QueueView(PermissionRequiredMixin, View):

    permission_required = [
        'dispatch_to_support.change_supportticket'
    ]

    raise_exception = True

    def get(self, request):
        return render(request, 'dispatch_to_support/get_case.html')

    def post(self, request):
        # return redirect()
        # dispatcher.populate_queue()
        sentiment, data = dispatcher.give_next_customer_case(give_to=self.request.user)
        feedback = data["feedback"]
        support_ticket = data["support_ticket"]
        context = {
            'gen': next(gen),
            'queue': dispatcher.queue.empty(),
            'sentiment': sentiment,
            'feedback': feedback,
        }
        # return render(request, 'dispatch_to_support/queue.html', context)
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
        # 'status',
    ]
    template_name = "dispatch_to_support/support_ticket_detail.html"
    success_url = reverse_lazy('dispatch_to_support:queue')

    def form_valid(self, form):
        form.instance.support_person = self.request.user
        form.instance.status = 1  # Closed
        form.instance.closed = timezone.localtime()
        return super(SupportTicketUpdateView, self).form_valid(form)

# from django.views.generic.edit import CreateView
# from myapp.models import Author

# class AuthorCreate(CreateView):
#     model = Author
#     fields = ['name']

#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super(AuthorCreate, self).form_valid(form)

class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        ctx = {
            'open_tickets': self.request.user.supportticket_set.filter(status=0)  # get open tickets
        }
        return render(request, 'dispatch_to_support/dashboard.html', ctx)
