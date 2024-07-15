from rest_framework.viewsets import ModelViewSet
from sistema.models import Post, Carrito
from sistema.api.serializers import PostSerializer
from sistema.api.serializers import ProductosSerializer
from sistema.api.serializers import CarritoSerializer
from sistema.models import Product
from rest_framework.views import APIView
from rest_framework import status
from django.db.utils import ProgrammingError
from rest_framework.response import Response

class PostApiViewSet(ModelViewSet): 
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CarritoApiViewSet(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Aquí va tu lógica para obtener los productos del carrito
            productos = Product.objects.all()
            # Serializa los datos de los productos
            serializer = ProductSerializer(productos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ProgrammingError:
            # Si ocurre un ProgrammingError, retornar una respuesta vacía
            return Response({"detail": "No hay productos en el carrito."}, status=status.HTTP_200_OK)

# Serializador
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
