from rest_framework.viewsets import ModelViewSet
from sistema.models import Post
from sistema.api.serializers import PostSerializer

class PostApiViewSet(ModelViewSet): 
    serializer_class = PostSerializer
    queryset = Post.objects.all()
