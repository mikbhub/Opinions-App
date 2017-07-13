from queue import PriorityQueue
from dispatch_to_support.models import SupportTicket
from django.utils import timezone

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
    
    
    # @staticmethod
    # # @property
    # def support_tickets():
        # return SupportTicket.objects.filter(status__isnull=True)

    def populate_queue(self):
        """
        Tries to populate inner priority queue with new tickets.
        Returns True if populated the queue with new records,
        False otherwise.
        """
        query_set = SupportTicket.objects.filter(status__isnull=True)
        print('Query set id: {}'.format(id(query_set)))
        if not query_set.exists():  # if query_set is empty
            print('The query set exists returned False')
            return False
        else:
            for support_ticket in query_set:
                sentiment = float(support_ticket.feedback.metrics.sentiment)
                time_lag = (timezone.localtime() - support_ticket.feedback.date).days
                priority_number = sentiment - time_lag
                print(f'appending to queue... with sentiment: {sentiment}, time_lag: {time_lag}, priority: {priority_number}')
                data = {
                    "feedback": support_ticket.feedback,
                    "support_ticket": support_ticket,
                }
                self.queue.put((priority_number, data))
            return True

    def give_next_customer_case(self, give_to, **kwargs):
        if self.queue.empty():
            print('Im empty')
            if self.populate_queue():
                print('queue populated')
                return self.give_next_customer_case(give_to, **kwargs)
            else:
                print('returning None')
                return 0, {
                    'feedback': None,
                    'support_ticket': None,
                }
        else:
            print('Im not empty, I hold {} items'.format(self.queue.qsize()))
            priority_number, data = self.queue.get()
            print('Getting next element from queue {}'. format(data))
            data["support_ticket"].status = 0
            data["support_ticket"].support_person = give_to
            data["support_ticket"].opened = timezone.localtime()
            data["support_ticket"].save()
            return priority_number, data
