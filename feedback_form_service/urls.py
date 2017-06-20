from django.conf.urls import url
from . views import FeebackForm

app_name = 'feedback_form_service'

urlpatterns = [
    url(r'^post-feedback/$', FeebackForm.as_view(), name='post-feedback'),

]
