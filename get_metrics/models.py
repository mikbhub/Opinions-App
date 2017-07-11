from django.db import models
from collect_opinions.models import Feedback
from django.dispatch import receiver


# Create your models here.
class Metrics(models.Model):

    feedback = models.ForeignKey(to=Feedback, null=True)
    sentiment = models.DecimalField(max_digits=4, decimal_places=3, null=True)

    class Meta:

        verbose_name = 'Metrics'
        verbose_name_plural = 'Metrics_list'

    def __str__(self):
        return f'Sentiment {self.sentiment} for feedback by {self.feedback}'
    
    # def get_absolute_url(self):
    #     """Return absolute url for Metrics."""
    #     return ('')


@receiver(models.signals.post_save, sender=Feedback)
def create_empty_metrics(instance, **kwargs):
    Metrics.objects.create(
        feedback=instance
    )
