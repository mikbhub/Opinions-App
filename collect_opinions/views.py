from django.http import Http404
from django.shortcuts import HttpResponse, redirect, render
from django.views import View, generic
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import FeedbackForm
from .models import Customer, Feedback
from .serializers import CustomerSerializer, FeedbackSerializer


# form-based views
class FeebackForm(generic.edit.FormView):

    def get(self, request):
        form = FeedbackForm()
        return render(
            request, 'collect_opinions/feedback_form.html', {'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            customer, created = Customer.objects.update_or_create(
                email=form.cleaned_data['email'],
                defaults={'name': form.cleaned_data['name']},
            )
            Feedback.objects.create(
                text=form.cleaned_data['text'],
                customer=customer,
            )
            return redirect('collect_opinions:form-success')
        else:
            return HttpResponse(f'The form was invalid<br>{form}')


class FormSuccess(generic.TemplateView):

    template_name = 'collect_opinions:form_success'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context


# api endpoints
class CustomerDetail(APIView):

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        customer = self.get_object(id)
        serializer = CustomerSerializer(customer, context={"request": request})
        return Response(serializer.data)


class CustomerList(APIView):

    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedbackView(APIView):

    def get_object(self, pk):
        try:
            return Feedback.objects.get(pk=pk)
        except Feedback.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        feedback = self.get_object(id)
        serializer = FeedbackSerializer(feedback, context={"request": request})
        return Response(serializer.data)


class FeedbackList(APIView):

    def get(self, request, format=None):
        feedbacks = Feedback.objects.all()
        serializer = FeedbackSerializer(feedbacks, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class CustomerView(APIView):

#     def get_object(self, pk):
#         try:
#             return Customer.objects.get(pk=pk)
#         except Customer.DoesNotExist:
#             raise Http404

#     def get(self, request, id, format=None):
#         customer = self.get_object(id)
#         serializer = CustomerSerializer(customer, context={"request": request})
#         return Response(serializer.data)

    # def delete(self, request, id, format=None):
    #     book = self.get_object(id)
    #     book.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def put(self, request, id, format=None):
    #     book = self.get_object(id)
    #     serializer = BookSerializer(book, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, id, format=None):
    #     pass
