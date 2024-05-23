from django.db import models

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
    Stock = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="products", null=True)
    categoria = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    
    def __str__(self):
        return self.nombre_producto

    

  


   

class Post(models.Model):
    Title = models.CharField(max_length=255)
    Content = models.TextField()


  

   