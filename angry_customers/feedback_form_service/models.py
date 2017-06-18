from django.db import models


# Create your models here.
class Customer(models.Model):

    email = models.EmailField(max_length=128, unique=True)
    name = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f'{self.name}, {self.email}'


class Feedback(models.Model):

    title = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(to=Customer, to_field='email', related_name="feedbacks_send")
    sentiment = models.DecimalField(max_digits=3, decimal_places=2, null=True)

    def __str__(self):
        return '{name}, {title}, {date}, {sentiment}'.format(
            name=self.customer.name,
            title=self.title,
            date=self.date,
            sentiment=self.sentiment,
        )
