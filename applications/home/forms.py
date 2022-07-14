from tkinter import Widget
from xml.dom.minidom import Attr
from django import forms
#models
from .models import Suscribers

class SuscribersForm(forms.ModelForm):
    class Meta:
        model= Suscribers
        fields = (
            'email',
        )
        widget={
            'email': forms.EmailInput(
                attrs = {
                    'placeholder': 'Correo electrónico ...',
                }
            ),
        }