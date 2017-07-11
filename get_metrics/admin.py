from django.contrib import admin
from get_metrics.models import Metrics
# Register your models here.


@admin.register(Metrics)
class MetricsAdmin(admin.ModelAdmin):
    '''
        Admin View for Metrics
    '''
    fields = [
        'feedback',
    ]
    list_display = [
        'sentiment',
        'feedback',
    ]
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
