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
        """
        Tries to populate inner priority queue with new tickets.
        Returns True if populated the queue with new records,
        False otherwise.
        """
        if not query_set.exists():  # if query_set is empty
            return False
        else:
            for support_ticket in query_set:
                priority_number = support_ticket.feedback.metrics.sentiment
                data = {
                    "feedback": support_ticket.feedback,
                    "support_ticket": support_ticket,
                }
                self.queue.put((priority_number, data))
            return True

    def give_next_customer_case(self):
        if self.queue.empty():
            # print('Im empty')
            if self.populate_queue():
                return self.give_next_customer_case()
                
            else:
                return 0, {
                    'feedback': None,
                    'support_ticket': None,
                }
        else:
            # print('Im not empty')
            priority_number, data = self.queue.get()
            data["support_ticket"].status=0
            data["support_ticket"].save()
            return priority_number, data
