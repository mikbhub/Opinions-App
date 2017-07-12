from django.conf.urls import url
from  dispatch_to_support import views


app_name = 'dispatch_to_support'

urlpatterns = [
    url(r'^queue/$', views.QueueView.as_view(), name='queue'),
    # url(r'^feedback-form/success/$', views.FormSuccess.as_view(), name='form-success'),
    # url(r'^feedback-form/failure/$', views.FeebackForm.as_view(), name='form-failure'),
    # url(r'^api/customers/$', views.CustomerListView.as_view(), name='customers'),
    # url(r'^api/customers/(?P<pk>(\d)+)', views.CustomerDetailView.as_view(), name='customer-detail'),
    # url(r'^api/customers/(?P<name>(\w)+)', views.CustomerDetailView.as_view(), name='api-customer-detail'),
    # url(r'^api/feedbacks/$', views.FeedbackListView.as_view(), name='customers'),
    # url(r'^api/feedbacks/(?P<pk>(\d)+)', views.FeedbackDetailView.as_view(), name='feedback-detail'),
]
