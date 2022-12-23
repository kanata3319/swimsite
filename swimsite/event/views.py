from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from event import models as e_models


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class ResultKojinListView(LoginRequiredMixin, ListView):
    model = e_models.IndividualEventResult
    template_name = 'home.html'


class ResultTaikaiListView(LoginRequiredMixin, ListView):
    model = e_models.IndividualEventResult
    template_name = 'home.html'
