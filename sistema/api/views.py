from rest_framework.viewsets import ModelViewSet
from sistema.models import Post
from sistema.api.serializers import PostSerializer
from sistema.api.serializers import ProductosSerializer
from sistema.models import Product

class PostApiViewSet(ModelViewSet): 
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class ProductosApiViewSet(ModelViewSet): 
    serializer_class = ProductosSerializer
    queryset = Product.objects.all()