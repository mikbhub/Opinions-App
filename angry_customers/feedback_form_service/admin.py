from django.contrib import admin
from . models import Customer, Feedback


class CustomerAdmin(admin.ModelAdmin):

    list_display = ('name', 'email',)
    search_fields = ['name', 'email',]
    list_filter = ['email',]


class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('customer', 'title', 'date',)
    search_fields = ['customer',]
    list_filter = ['date', 'customer',]


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Feedback, FeedbackAdmin)
