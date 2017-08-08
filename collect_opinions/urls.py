from django.conf.urls import url
from  collect_opinions import views


app_name = 'collect_opinions'

urlpatterns = [
    url(r'^feedback-form/$', views.FeebackFormView.as_view(), name='feedback-form'),
    url(r'^feedback-form/success/$', views.FormSuccess.as_view(), name='form-success'),
    # url(r'^feedback-form/failure/$', views.FeebackForm.as_view(), name='form-failure'),
    url(r'^api/customers/$', views.CustomerListView.as_view(), name='customers'),
    url(r'^api/customers/(?P<pk>(\d)+)', views.CustomerDetailView.as_view(), name='customer-detail'),
    # url(r'^api/customers/(?P<name>(\w)+)', views.CustomerDetailView.as_view(), name='api-customer-detail'),
    url(r'^api/feedbacks/$', views.FeedbackListView.as_view(), name='feedbacks'),
    url(r'^api/feedbacks/(?P<pk>(\d)+)', views.FeedbackDetailView.as_view(), name='feedback-detail'),
    url(r'^api/feedbacks/new/$', views.FeedbackCreateView.as_view(), name='feedback-create'),
]
