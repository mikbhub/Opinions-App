from django.conf.urls import url
from  collect_opinions import views


app_name = 'collect_opinions'

urlpatterns = [
    url(r'^feedback-form/$', views.FeebackForm.as_view(), name='feedback-form'),
    url(r'^feedback-form/success/$', views.FormSuccess.as_view(), name='form-success'),
    url(r'^feedback-form/failure/$', views.FeebackForm.as_view(), name='form-failure'),
    url(r'^api/customers/$', views.CustomerList.as_view(), name='api-customers'),
    url(r'^api/customers/(?P<id>(\d)+)', views.CustomerDetail.as_view(), name='api-customer-detail'),
    url(r'^api/feedbacks/$', views.FeedbackList.as_view(), name='api-customers'),
    url(r'^api/feedbacks/(?P<id>(\d)+)', views.FeedbackView.as_view(), name='api-feedback-detail'),
]
