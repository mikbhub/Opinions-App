from django.db import models


# Create your models here.
class Customer(models.Model):

    email = models.EmailField(max_length=128, unique=True, null=True, db_index=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}, {self.email}'


class Feedback(models.Model):

    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(to=Customer, related_name="feedbacks_send")
    source = models.CharField(max_length=128)
    # sentiment = models.DecimalField(max_digits=4, decimal_places=3, null=True)

    def __str__(self):
        return 'Cutomer {name}, posted on {date} via {source} '.format(
            name=self.customer.name,
            date=self.date,
            source=self.source,
        )
