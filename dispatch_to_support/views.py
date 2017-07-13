from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView, UpdateView

from dispatch_to_support.dispatcher import CustomerSupportDispatcher
from dispatch_to_support.models import SupportTicket


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
        sentiment, data = dispatcher.give_next_customer_case()
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
            return redirect('dispatch_to_support:ticked-detail', pk=support_ticket.pk)
        except AttributeError:
            return render(request, 'dispatch_to_support/queue.html', context)


class SupportTicketDetailView(DetailView):
    model = SupportTicket
    template_name = "dispatch_to_support/support_ticket_detail.html"



class SupportTicketUpdateView(UpdateView):
    model = SupportTicket
    template_name = "TEMPLATE_NAME"
