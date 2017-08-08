from queue import PriorityQueue
from dispatch_to_support.models import SupportTicket
from django.utils import timezone

class CustomerSupportDispatcher:
    """
    customer support person requests next support case
    dispatcher tries to provide next element from it's queue
    if it fails, it populates it's queue by quering the database for feedback that has not been processed by customer support
    it queries from ordered by -date
    """

    def __init__(self, *args, **kwargs):
        self.queue = PriorityQueue()

    def populate_queue(self):
        """
        Tries to populate inner priority queue with new tickets.
        Returns True if populated the queue with new records,
        False otherwise.
        """
        query_set = SupportTicket.objects.filter(status__isnull=True)
        if not query_set.exists():  # if query_set is empty, there are no more tickets to process.
            return False
        else:
            # build inner PriorityQueue from tuples:
            # (sentiment, data)
            for support_ticket in query_set:
                sentiment = float(support_ticket.feedback.metrics.sentiment)
                time_lag = (timezone.localtime() - support_ticket.feedback.date).days
                priority_number = sentiment - time_lag
                data = {
                    "feedback": support_ticket.feedback.pk,
                    "support_ticket": support_ticket.pk,
                    "sentiment": sentiment,
                }
                self.queue.put((priority_number, data))
            return True

    def give_next_customer_case(self, give_to, **kwargs):
        # batch-populate inner queue if it is empty
        if self.queue.empty():
            # once the inner queue is populated, do a recursion
            if self.populate_queue():
                return self.give_next_customer_case(give_to, **kwargs)
            else:
                # TODO: un-ugly this
                return None, None
        else:
            priority_number, data = self.queue.get()
            SupportTicket.objects.filter(pk=data["support_ticket"]).update(
                status=0,
                support_person=give_to,
                opened=timezone.localtime(),
            )
            return priority_number, data
