from django.contrib import admin
from . models import Customer, Feedback


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('name', 'email',)
    search_fields = ['name', 'email',]
    list_filter = ['email',]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('customer', 'date', 'source',)
    search_fields = ['customer',]
    list_filter = ['date', 'customer', 'source',]
