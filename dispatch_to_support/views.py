from django.shortcuts import render
from django.views import View
from dispatch_to_support.dispatcher import CustomerSupportDispatcher

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
        sentiment, feedback = dispatcher.give_next_customer_case()
        context = {
            'gen': next(gen),
            'queue': dispatcher.queue.empty(),
            'sentiment': sentiment,
            'feedback': feedback,
        }
        return render(request, 'dispatch_to_support/queue.html', context)
