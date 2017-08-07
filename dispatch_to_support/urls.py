from django.conf.urls import url
from  dispatch_to_support import views


app_name = 'dispatch_to_support'

urlpatterns = [
    url(r'^queue/$', views.QueueView.as_view(), name='queue'),
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^ticked_detail/(?P<pk>(\d)+)$', views.SupportTicketDetailView.as_view(), name='ticket-detail'),
    url(r'^ticked_update/(?P<pk>(\d)+)$', views.SupportTicketUpdateView.as_view(), name='ticket-update'),
    url(r'^response_create/(?P<ticket_pk>(\d)+)$', views.ResponseCreateView.as_view(), name='response-create'),
    url(r'^response_detail/(?P<pk>(\d)+)$', views.ResponseDetailView.as_view(), name='response-detail'),
]
