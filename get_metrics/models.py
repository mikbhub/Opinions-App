from django.db import models


# Create your models here.
class Metrics(models.Model):
    """Model definition for Metrics."""

    sentiment = models.DecimalField(max_digits=4, decimal_places=3, null=True)
