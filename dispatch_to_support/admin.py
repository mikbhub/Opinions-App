from django.contrib import admin
from dispatch_to_support.models import SupportTicket


# Register your models here.
@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    '''
        Admin View for SupportTicket
    '''
    list_display = (
        'feedback',
        'status',
        'opened',
        'closed',
    )
    list_filter = (
        'status',
        'opened',
        'closed',
    )
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)


