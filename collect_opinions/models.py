from django.db import models


class Customer(models.Model):
    """
    Customers share their opinions on the web, in social media
    and via contact forms.
    """

    email = models.EmailField(max_length=128, unique=True, null=True, db_index=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}, email: {self.email}'

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class FeedbackManager(models.Manager):
    """
    Encapsulates Feedback creation and updating.
    """
    
    # TODO: implement 'create' method that creates or updates customer instance realted to feedback instance
    def create_feedback_from_Form_or_Api(self, email, name, **feedback_kwargs):
        """
        Creates new Feedback instance and assigns it to Customer from the database.
        If customer is not in the database, creates Customer instance and saves it to the database.
        """
        customer, created = Customer.objects.update_or_create(
                email=email,
                defaults={'name': name},
            )
        feedback_kwargs.update({'customer': customer})
        feedback = Feedback.objects.create(**feedback_kwargs)
        return feedback


class Feedback(models.Model):
    """
    Opinion shared by a customer.
    """

    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(to=Customer, related_name="feedbacks_send")
    source_type = models.CharField(max_length=128, null=True)  # contact form, facebook, twitter etc.
    source_url = models.CharField(max_length=400, null=True)  # internet location
    location = models.CharField(max_length=60, null=True, blank=True)  # geolocation

    objects = FeedbackManager()

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
