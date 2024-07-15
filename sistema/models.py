from django.db import models
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _
from django.utils import timezone
import requests
# Create your models here.

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    descripcion_producto = models.TextField()
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    stock_producto = models.IntegerField()
    imagen_producto = models.ImageField(upload_to='productos/')
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
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

   

    


  

   