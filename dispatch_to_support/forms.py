from django import forms
from dispatch_to_support.models import SupportTicket, Response
# from django.utils.translation import ugettext_lazy as _


class SupportTicketForm(forms.Form):

    response = forms.TextInput()

    name = forms.CharField(max_length=128)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


# class FeedbackForm(forms.ModelForm):

#     # customer = forms.EmailField()

#     class Meta:
#         model = Feedback
#         fields = (
#             'title',
#             'description',
#             'customer',
#         )

#         labels = {
#             'customer': _('Your email'),
#         }

#         help_texts = {
#             'description': _('Please describe your problem.'),
#         }

#         # widgets = {
#         #     'customer': forms.EmailInput(),
#         # }
