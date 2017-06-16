from django.shortcuts import render, HttpResponse
from django.views import View
from django.views import generic
from .forms import FeedbackForm


class FeebackForm(generic.FormView):

    def get(self, request):
        form = FeedbackForm()
        return render(request, 'feedback_form_service/feedback_form.html', {'form': form})
        # return HttpResponse('Viewing GET')

    def post(self, request):
        return HttpResponse('Viewing POST')
