from django.contrib import admin
from . models import Customer, Feedback


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('name', 'email',)
    search_fields = ['name', 'email',]
    # list_filter = ['email',]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    def customer_name(self, obj):
        return obj.customer.name

    def customer_email(self, obj):
        return obj.customer.email

    list_display = ('customer_name', 'customer_email', 'date', 'source_type',)
    search_fields = ['customer',]
    list_filter = ['date', 'source_type',]
