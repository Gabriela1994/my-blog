from django import forms
from django.contrib.auth import authenticate
#
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        help_text='Ingrese una contraseña numérica de al menos 8 dígitos',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            'email',
            'full_name',
            'ocupation',
            'genero',
            'date_birth',
        )
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electrónico',
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres y apellidos',
                }
            ),
            'ocupation': forms.TextInput(
                attrs={
                    'placeholder': 'Ocupación',
                }
            ),
            'date_birth': forms.DateInput(
                attrs={
                    'type':'date',
                }
            ),
        }
    
    # def clean_password2(self):
    #     if self.cleaned_data['password1'] != self.cleaned_data['password2']:
    #         self.add_error('password2', 'Las contraseñas no coinciden')
    def clean_full_name(self):
        full_name= self.cleaned_data['full_name']
        
        if not full_name.isalpha():
            raise forms.ValidationError('Solo puedes ingresar carácteres alfabéticos.')
        return full_name
    
    def clean_ocupation(self):
        ocupation= self.cleaned_data['ocupation']
        
        if not ocupation.isalpha():
            raise forms.ValidationError('Solo puedes ingresar carácteres alfabéticos.')
        return ocupation

    def clean_email(self):
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('Esta dirección de correo electrónico ya está en uso.')
        return email
        
    def clean_password2(self):
        """verificar si ambas contraseñas coinciden"""
        password1= self.cleaned_data['password1']
        password2= self.cleaned_data['password2']

        if password1 != password2:            
            self.add_error('password2', 'Las contraseñas no coinciden.')

        if len(password1) < 8:
            self.add_error('password1', 'La contraseña debe contener mínimo 8 carácteres.')


class LoginForm(forms.Form):
    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Correo Electronico',
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            self.add_error('password', 'La contraseña es incorrecta.')
            self.add_error('email', 'El correo electrónico que ingresaste no existe.')
        #    raise forms.ValidationError('Los datos de usuario no son correctos')        
        return self.cleaned_data


class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )