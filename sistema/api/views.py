from rest_framework.viewsets import ModelViewSet
from sistema.models import Post, Carrito
from sistema.api.serializers import PostSerializer
from sistema.api.serializers import ProductosSerializer
from sistema.api.serializers import CarritoSerializer
from sistema.models import Product


class PostApiViewSet(ModelViewSet): 
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class ProductosApiViewSet(ModelViewSet): 
    serializer_class = ProductosSerializer
    queryset = Product.objects.all()

class CarritoApiViewSet(ModelViewSet):
    serializer_class = CarritoSerializer
    queryset = Carrito.objects.all()
