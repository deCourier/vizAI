from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class InnerView(generic.ListView):
    template_name = 'inner-page.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]



class CancerView(generic.ListView):
    model = Question
    template_name = 'cancer.html'

class AlcoholView(generic.ListView):
    model = Question
    template_name = 'alcohol.html'

class HousingView(generic.ListView):
    model = Question
    template_name = 'housing.html'

class UnemploymentView(generic.ListView):
    model = Question
    template_name = 'unemployment.html'

class NBAView(generic.ListView):
    model = Question
    template_name = 'nba.html'


class DiabetesView(generic.ListView):
    model = Question
    template_name = 'diabetes.html'
