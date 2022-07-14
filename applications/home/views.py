import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView,
)
#apps entrada
from applications.entrada.models import Entry
#models
from .models import Home
#forms
from .forms import SuscribersForm

class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        #cargamos el home, en base al ultimo registro creado
        context["home"] = Home.objects.latest('created')
        #contexto de portada (entrada_en_portada es un manager)
        context["portada"] = Entry.objects.entrada_en_portada()
        #contexto para los articulos
        context["entradas_home"] = Entry.objects.entradas_en_home()
        #contexto para las entradas recientes
        context['entradas_recientes'] = Entry.objects.entradas_recientes()
        #enviamos formulario de suscripcion
        context["suscripcion"] = SuscribersForm
        return context

class SuscriberCreateView(CreateView):
    form_class = SuscribersForm
    success_url = '.'