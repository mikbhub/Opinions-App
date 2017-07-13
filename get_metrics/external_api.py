# import requests
from django.dispatch import receiver
from django.db import models

from get_metrics.models import Metrics
from get_metrics.nltk_sentiment import analyze_sentiment_using_vader


def fill_null_metrics_using_vader():
    metrics_to_fill = Metrics.objects.filter(sentiment__isnull=True)
    for metric in metrics_to_fill:
        text = metric.feedback.text
        metric.sentiment = analyze_sentiment_using_vader(text)
        metric.save()


# @receiver(models.signals.post_save, sender=Metrics)
# def vader_signal(instance, **kwargs):
#     print('received signal form {}'.format(instance))
    # fill_null_metrics_using_vader()
# def fill_null_metrics_using_vader(instance, **kwargs):
#         text = instance.feedback.text
#         instance.sentiment = analyze_sentiment_using_vader(text)
#         instance.save()

# def create_empty_metrics(instance, **kwargs):
#     Metrics.objects.create(
#         feedback=instance
#     )