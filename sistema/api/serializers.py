from rest_framework.serializers import ModelSerializer
from sistema.models import Post
from sistema.models import Product
from sistema.models import Carrito
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.decorators import action


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ProductosSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CarritoSerializer(ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'

   

