from django import forms
from dispatch_to_support.models import SupportTicket, Response


class SupportTicketForm(forms.Form):

    response = forms.TextInput()

    name = forms.CharField(max_length=128)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


class ResponseForm(forms.ModelForm):

    class Meta:
        model = Response
        fields = (
            'text',
        )
