from queue import PriorityQueue
from dispatch_to_support.models import SupportTicket


class CustomerSupportDispatcher:
    """
    customer support person requests next support case
    dispatcher tries to provide next element from it's queue
    if it fails, it populates it's queue by quering the database for feedback that has not been processed by customer support
    it queries from ordered by -date
        on service 'cold' start it does the same, after sleeping for 60 sec.

    How and when are the metrics populated?
    """

    def __init__(self, *args, **kwargs):
        self.queue = PriorityQueue()
        # super(CLASS_NAME, self).__init__(*args, **kwargs)

    def populate_queue(self, query_set=SupportTicket.objects.filter(status__isnull=True)):
        if query_set.exists():  # if query_set is not empty
            for item in query_set:
                priority_number = item.feedback.metrics.sentiment
                data = item.feedback
                self.queue.put((priority_number, data))

    def give_next_customer_case(self):
        if self.queue.empty():
            # print('Im empty')
            self.populate_queue()
            return self.give_next_customer_case()
        else:
            # print('Im not empty')
            return self.queue.get()
