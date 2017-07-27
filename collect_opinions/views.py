from django.http import Http404
from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse_lazy
from django.views import View, generic
from rest_framework import generics as rest_generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from collect_opinions.forms import FeedbackForm
from collect_opinions.models import Customer, Feedback
from collect_opinions.serializers import (
    CustomerSerializer,
    FeedbackCreateSerializer,
    FeedbackSerializer
)


# form-based views
class FeebackForm(generic.edit.FormView):

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


# api endpoints
class CustomerDetailView(rest_generics.RetrieveUpdateDestroyAPIView):
    # lookup_field = (
    #     'name'
    # )
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerListView(rest_generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class FeedbackDetailView(rest_generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackListView(rest_generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackCreateView(rest_generics.CreateAPIView):
    serializer_class = FeedbackCreateSerializer


# TODO: create cutomer if does not exist in the database
# class FeedbackView(APIView):

#     def get_object(self, pk):
#         try:
#             return Feedback.objects.get(pk=pk)
#         except Feedback.DoesNotExist:
#             raise Http404

#     def get(self, request, id, format=None):
#         feedback = self.get_object(id)
#         serializer = FeedbackSerializer(feedback, context={"request": request})
#         return Response(serializer.data)


# class FeedbackList(APIView):

#     def get(self, request, format=None):
#         feedbacks = Feedback.objects.all()
#         serializer = FeedbackSerializer(feedbacks, many=True, context={"request": request})
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = FeedbackSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
