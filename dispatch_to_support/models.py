from django.db import models
from django.dispatch import receiver
from django.urls import reverse

from collect_opinions.models import Feedback


# Create your models here.
class SupportTicket(models.Model):
    """Model definition for SupportTicket."""

    STATUS = (
        (0, 'open'),
        (1, 'closed'),
    )

    # TODO: Define fields here
    # is tied to feedback
    feedback = models.ForeignKey(to=Feedback, null=True, related_name='support_tickets_issued')
    # status: open (is opened when customer suport first takes care of it) or closed
    status = models.IntegerField(choices=STATUS, null=True, blank=True)
    # date open 
    opened = models.DateTimeField(null=True, blank=True)
    # date close
    closed = models.DateTimeField(null=True, blank=True)


    class Meta:
        """Meta definition for SupportTicket."""

        verbose_name = 'SupportTicket'
        verbose_name_plural = 'SupportTickets'

    def __str__(self):
        return 'Status: {status}, {feedback}'.format(
            status=self.get_status_display(),
            feedback=self.feedback
        )
    
    def get_absolute_url(self):
        return reverse('dispatch_to_support:ticket-detail', kwargs={'pk': self.pk})


@receiver(models.signals.post_save, sender=Feedback)
def create_empty_metrics(instance, **kwargs):
    SupportTicket.objects.create(
        feedback=instance
    )
