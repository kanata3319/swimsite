from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import resolve_url
from django.views.generic import TemplateView, FormView, CreateView
from event import forms as e_forms
from event import models as e_models


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class ResultKojinFormView(LoginRequiredMixin, FormView):
    """個人記録"""
    template_name = 'record_kojin.html'
    form_class = e_forms.RecordKojinForm

    def form_valid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['is_search'] = self.request.method == 'POST'
        if 'form' not in kwargs:
            return context

        form = kwargs['form']
        player = form.cleaned_data['player']
        competition = form.cleaned_data['competition']
        inv_qs = e_models.IndividualEventResult.objects.filter(player=player).order_by('-competition__event_date','competition', 'event')
        relay_q = (Q(player_1=player) | Q(player_2=player) | Q(player_3=player) | Q(player_4=player))
        relay_qs = e_models.RelayEventResult.objects.filter(relay_q).order_by('-competition__event_date','competition', 'event')
        if competition:
            relay_qs = relay_qs.filter(competition=competition)
            inv_qs = inv_qs.filter(competition=competition)
        context['inv_qs'] = inv_qs
        context['relay_qs'] = relay_qs

        return context


class ResultTaikaiListView(LoginRequiredMixin, FormView):
    """大会記録"""
    template_name = 'record_taikai.html'
    form_class = e_forms.RecordTaikaiForm

    def form_valid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['is_search'] = self.request.method == 'POST'
        if 'form' not in kwargs:
            return context

        form = kwargs['form']
        competition = form.cleaned_data['competition']
        inv_qs = e_models.IndividualEventResult.objects.filter(competition=competition).order_by('event','time')
        relay_qs = e_models.RelayEventResult.objects.filter(competition=competition).order_by('event','time')
        context['inv_qs'] = inv_qs
        context['relay_qs'] = relay_qs

        return context


class ResultKojinCreateView(LoginRequiredMixin, CreateView):
    """大会記録"""
    template_name = 'result_kojin_create.html'
    form_class = e_forms.RecordCreateKojinForm

    def get_success_url(self):
        messages.success(self.request, '登録しました。')
        return resolve_url('result_kojin_create')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        cl = form.cleaned_data
        time_minute = cl['time_minute'] * Decimal('60')
        time_mili_second = cl['time_mili_second']
        time_mili_second = time_mili_second * Decimal('0.01')
        self.object.time = time_minute + cl['time_second'] + time_mili_second
        return super().form_valid(form)