from django import forms
from . models import Feedback


class FeedbackForm(forms.Form):

    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
