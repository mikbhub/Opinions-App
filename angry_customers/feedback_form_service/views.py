from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.views import generic
from .forms import FeedbackForm
from .models import Customer, Feedback


class FeebackForm(generic.edit.FormView):

    def get(self, request):
        form = FeedbackForm()
        return render(request, 'feedback_form_service/feedback_form.html', {'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            customer, created = Customer.objects.update_or_create(
                email=form.cleaned_data['customer'],
                defaults={'name': form.cleaned_data['name']},
            )
            Feedback.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                customer=customer,
            )
            return HttpResponse(f'Viewing POST valid form<br>{form}')
        else:
            return HttpResponse('The form was invalid<br>{form}')
