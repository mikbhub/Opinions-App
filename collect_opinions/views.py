from django.http import Http404
from django.shortcuts import HttpResponse, redirect, render
from django.views import View, generic
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from collect_opinions.forms import FeedbackForm
from collect_opinions.models import Customer, Feedback
from collect_opinions.serializers import CustomerSerializer, FeedbackSerializer


# form-based views
class FeebackForm(generic.edit.FormView):

    def get(self, request, *args, **kwargs):
        form = FeedbackForm()
        return render(request, 'collect_opinions/feedback_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            customer, created = Customer.objects.update_or_create(
                email=form.cleaned_data['email'],
                defaults={'name': form.cleaned_data['name']},
            )
            Feedback.objects.create(
                text=form.cleaned_data['text'],
                customer=customer,
                source='legacy-form'
            )
            return redirect('collect_opinions:form-success')
        else:
            return HttpResponse(f'The form was invalid<br>{form}')


# api endpoints
class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    # lookup_field = (
    #     'name'
    # )
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# TODO: create cutomer if does not exist in the database
class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


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

class FeedbackListView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

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
