from django.db import models
#app terceros
from model_utils.models import TimeStampedModel

class Home(TimeStampedModel):
    """Modelo de pagina principal"""

    tittle = models.CharField('Nombre', max_length=30)
    description = models.TextField()
    about_title = models.CharField('Sobre Nosotros', max_length=50)
    about_text = models.TextField()
    contact_email = models.EmailField('Email de contacto', blank=True, null=True)
    phone = models.CharField('Telefono de contacto', max_length=20)

    class Meta:
        verbose_name = 'Pagina principal'
        verbose_name_plural = 'Paginas principales'
    
    def __str__(self):
        return self.tittle

class Suscribers(TimeStampedModel):
    """Modelo de suscriptores"""

    email = models.EmailField()

    class Meta:
        
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'
    
        def __str__(self):
            return self.email
    
class Contact(TimeStampedModel):
    
    full_name = models.CharField('Nombres', max_length=60)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'
    
        def __str__(self):
            return self.full_name

