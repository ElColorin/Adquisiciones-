from django.urls import path
from .import views
from rest_framework.documentation import include_docs_urls
from .views import login_view, logout_view


urlpatterns = [
    path('', views.index, name='index'),
    path('filter/', views.filter_products, name='filter_products'),
    path('agregar/<int:product_id>/', views.agregar_producto, name='agregar_producto'),
    path('carrito/', views.ver_carro, name='ver_carro'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar_producto'),
    path('procesar_compra/', views.procesar_compra, name='procesar_compra'),
    path('docs1/', include_docs_urls(title='Documentacion de la api')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('productos/', views.index, name='productos'),
    #path('agregar/<int:product_id>/', views.agregar_producto, name='agregar_producto'),
    #path('carrito/', views.ver_carro, name='ver_carro'),
    #path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    #path('product/product_id>/', views.detalle, name='product_detail'),

    
  
]
