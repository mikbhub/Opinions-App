from django.db import models


# Create your models here.
class Customer(models.Model):

    email = models.EmailField(max_length=128, unique=True, null=True, db_index=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}, email: {self.email}'

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class Feedback(models.Model):

    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(to=Customer, related_name="feedbacks_send")
    source_type = models.CharField(max_length=128, null=True)
    source_url = models.CharField(max_length=400, null=True)

    @property
    def short_text(self):
        return self.text[:10]

    def __str__(self):
        return '{short_text}, customer: {name}, posted on {date} via {source} '.format(
            short_text=self.short_text,
            name=self.customer.name,
            date=self.date,
            source=self.source_type,
        )
    
    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
