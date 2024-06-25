from django.db import models
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _

# Create your models here.

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model):
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="products", null=True)
    categoria = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    
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


  

   