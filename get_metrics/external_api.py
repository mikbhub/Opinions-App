# import requests
from get_metrics.models import Metrics
from get_metrics.nltk_sentiment import analyze_sentiment_using_vader


def fill_null_metrics():
    metrics_to_fill = Metrics.objects.filter(sentiment__isnull=True)
    for metric in metrics_to_fill:
        text = metric.feedback.text
        metric.sentiment = analyze_sentiment_using_vader(text)
        metric.save()
