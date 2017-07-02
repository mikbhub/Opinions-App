from django.conf.urls import url
from . views import FeebackForm

app_name = 'collect_opinions'

urlpatterns = [
    url(r'^post-feedback/$', FeebackForm.as_view(), name='post-feedback'),

]
