from rest_framework.serializers import ModelSerializer
from sistema.models import Post
from sistema.models import Product

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ProductosSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'