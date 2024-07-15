from rest_framework.viewsets import ModelViewSet
from sistema.models import Post, Carrito
from sistema.api.serializers import PostSerializer
from sistema.api.serializers import CarritoSerializer



class PostApiViewSet(ModelViewSet): 
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CarritoApiViewSet(ModelViewSet):
    serializer_class = CarritoSerializer
    queryset = Carrito.objects.all()
