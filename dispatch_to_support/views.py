from django.shortcuts import render
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
class QueueView(View):

    def get(self, request):
        # dispatcher.populate_queue()
        sentiment, data = dispatcher.give_next_customer_case()
        feedback = data["feedback"]
        context = {
            'gen': next(gen),
            'queue': dispatcher.queue.empty(),
            'sentiment': sentiment,
            'feedback': feedback,
        }
        return render(request, 'dispatch_to_support/queue.html', context)



class SupportTicketDetailView(DetailView):
    model = SupportTicket
    template_name = "dispatch_to_support/support_ticket_detail.html"
