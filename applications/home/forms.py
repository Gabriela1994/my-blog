from django import forms
#models
from .models import Suscribers, Contact

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

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')

        def clean(self):
            """Validaciones para el formulario"""
            usuario= self.cleaned_data['full_name']
            correo= self.cleaned_data['email']
            mensaje= self.cleaned_data['message']
        
            if len(usuario) < 1:
                self.add_error('usuario', 'No puedes enviar un mensaje vacio')
            if len(correo) < 1:
                self.add_error('correo', 'No puedes enviar un mensaje vacio')
            if len(mensaje) < 1:
                self.add_error('mensaje', 'No puedes enviar un mensaje vacio')