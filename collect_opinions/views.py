from django.shortcuts import HttpResponse, redirect, render
from django.views import View, generic
from rest_framework import generics as rest_generics

from collect_opinions.forms import FeedbackForm
from collect_opinions.models import Customer, Feedback
from collect_opinions.serializers import (
    CustomerSerializer,
    FeedbackCreateSerializer,
    FeedbackSerializer
)

# form-based views
class FeebackForm(generic.edit.FormView):
    """
    Form for posting new feedback.
    """

    def get(self, request, *args, **kwargs):
        form = FeedbackForm()
        return render(request, 'collect_opinions/feedback_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Feedback.objects.create_feedback_from_Form_or_Api(
                email=form.cleaned_data['email'],
                name=form.cleaned_data['name'],
                text=form.cleaned_data['text'],
                source_type='legacy-form',
                source_url=request.build_absolute_uri(),
            )
            return redirect('collect_opinions:form-success')
        else:
            return HttpResponse(f'The form was invalid<br>{form}')


class FormSuccess(View):
    def get(self, request):
        return render(request, 'collect_opinions/form_success.html')


# Api endpoints
class CustomerDetailView(rest_generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a 'customer' instance.
    """
    # lookup_field = (
    #     'name'
    # )
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerListView(rest_generics.ListCreateAPIView):
    """
    List all `customers` or create new `customer`.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class FeedbackDetailView(rest_generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a 'feedback' instance.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackListView(rest_generics.ListAPIView):
    """
    List all `feedbacks` from the database.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackCreateView(rest_generics.CreateAPIView):
    """
    Create a new `feedback` instance, assign it to `customer`
    and, if one is not in the database, create new `customer` .
    """
    serializer_class = FeedbackCreateSerializer
