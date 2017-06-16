from django import forms
from . models import Feedback
from django.utils.translation import ugettext_lazy as _


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = (
            'title',
            'description',
            'customer',
        )

        labels = {
            'customer': _('Your email'),
        }

        help_texts = {
            'description': _('Please describe your problem.'),
        }

        widgets = {
            'customer': forms.EmailInput(),
        }
