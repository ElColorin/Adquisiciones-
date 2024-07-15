from django.db import models
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _
from django.utils import timezone
import requests
# Create your models here.

from django.db import models

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria
    



class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    descripcion_producto = models.TextField()
    stock_producto = models.IntegerField()
    precio_producto = models.IntegerField()
    imagen_producto = models.ImageField(upload_to="products", null=True)
    categoria_id_categoria = models.IntegerField()
    
    
    def __str__(self):
        return self.nombre_producto
    

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label=_("Nombre de usuario"), max_length=150)
    password = forms.CharField(label=_("Contraseña"), strip=False, widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': _(
            "Por favor, asegúrate de que los datos ingresados son correctos. "
            "Ambos campos pueden ser sensibles a mayúsculas y minúsculas."
        ),
        'inactive': _("Esta cuenta está inactiva."),
    }

   
class Post(models.Model):
    Title = models.CharField(max_length=255)
    Content = models.TextField()


class Carrito(models.Model):
    fecha_adquisicion = models.DateTimeField(auto_now_add=True)
    cantidad_total = models.IntegerField()
    productos = models.ManyToManyField('Product', related_name='carritos')
    precio = models.IntegerField()

    # Otros campos y métodos si los tienes


    def __str__(self):
        return f'Carrito {self.id}'

   

    


  

   