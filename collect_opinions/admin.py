from django.contrib import admin
from collect_opinions.models import Customer, Feedback


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    def opinions(self, obj):
        return obj.feedbacks_send.count()

    list_display = ('name', 'email', 'opinions',)
    search_fields = ['name', 'email',]
    # list_filter = ['opinions',]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    def customer_name(self, obj):
        return obj.customer.name

    def customer_email(self, obj):
        return obj.customer.email

    def sentiment(self, obj):
        return obj.metrics.sentiment

    def short_text(self, obj):
        return obj.text[:15]

    list_display = (
        'short_text',
        'customer_name',
        'customer_email',
        'date',
        'source_type',
        'sentiment',
    )
    search_fields = ['customer',]
    list_filter = ['date', 'source_type',]
