from rest_framework.routers import DefaultRouter
from sistema.api.views import PostApiViewSet
from sistema.api.views import ProductosApiViewSet


router_posts = DefaultRouter()
router_producto = DefaultRouter()

router_posts.register(prefix='post', basename='post', viewset=PostApiViewSet)
router_producto.register(prefix='productos', basename='productos', viewset=ProductosApiViewSet)