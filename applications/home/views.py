
from django.urls import reverse_lazy

from django.views.generic import (
    TemplateView,
    CreateView,
)
from django.contrib.messages.views import SuccessMessageMixin
#apps entrada
from applications.entrada.models import Entry
#models
from .models import Home
#forms
from .forms import SuscribersForm, ContactForm

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

class ContactCreateView(SuccessMessageMixin, CreateView):
    template_name = "home/index.html"
    form_class = ContactForm
    success_url = reverse_lazy("home_app:index")
    success_message = 'Mensaje enviado correctamente'
