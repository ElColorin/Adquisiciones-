from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Product, Category, CustomAuthenticationForm, Carrito
from .carro import Carro
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
import requests
from django.utils import timezone



def index(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(nombre_producto__icontains=query)
    else:
        products = Product.objects.all()
    
    categories = Category.objects.all()
    data = {
        'categories': categories,
        'products': products,
        'query': query,
    }
    return render(request, 'sistema/index.html', data)

def filter_products(request):
    category_name = request.GET.get('category')
    if category_name and category_name != 'all':
        products = Product.objects.filter(categoria__name__iexact=category_name)
    else:
        products = Product.objects.all()

    products_data = [{
        'nombre': product.nombre_producto,
        'descripcion': product.descripcion,
        'precio': product.precio,
        'imagen_url': product.imagen.url,
        'category': product.categoria.name,
    } for product in products]

    return JsonResponse({'products': products_data})

#ef detalle(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'sistema/detalle.html', {'product': product})


def agregar_producto(request, product_id):
    carro = Carro(request)
    producto = get_object_or_404(Product, id=product_id)
    carro.agregar(producto)
    return redirect('index')

def ver_carro(request):
    carro = Carro(request)
    return render(request, 'sistema/carrito.html', {'carro': carro})

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    try:
        producto = Product.objects.get(id=producto_id)
        carro.eliminar(producto)
        messages.success(request, f'{producto.nombre_producto} ha sido eliminado del carrito.')
    except Product.DoesNotExist:
        # Si el producto no existe, lo eliminamos directamente del carrito
        del carro.carro[str(producto_id)]
        messages.error(request, 'El producto no existe, pero ha sido eliminado del carrito.')
    return redirect('ver_carro')

def restar_producto(request, producto_id):
    producto = get_object_or_404(Product, pk=producto_id)
    carro = Carro(request)
    carro.restar(producto)
    return redirect('ver_carro')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('admin.adquisiciones')
        password = request.POST.get('adquisiciones')
        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZHF1aXNpY2lvbmVzIjoidG9rZW5fYWRxdWlzaWNpb25lcyJ9.8cKAY45kC9w9gJAp2a_h99A4RZJEuFcExBcoVfwZIc0'
        
        # Datos para la solicitud POST
        data = {
            'username': username,
            'password': password,
            'token': token
        }
        
        headers = {
            'content-type': 'aplication/json',
        }

        # URL del endpoint de validación
        url = 'https://qic534o8o0.execute-api.us-east-1.amazonaws.com/validacionUsuarios/'
        
        # Realizar la solicitud POST
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            result = response.json()
            if result.get('valid', False):
                # Iniciar sesión en el sistema
                messages.success(request, 'Inicio de sesión exitoso')
                return redirect('index')  
            else:
                messages.error(request, 'Credenciales inválidas')
        else:
            messages.error(request, 'Error en la validación de usuario')
        
    return render(request, 'sistema/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente')
    return redirect('index')  # Redirige a la página principal de productos después del logout


GITHUB_RAW_URL = 'https://raw.githubusercontent.com/ElColorin/Adquisiciones-/Django/stock.json'

def cargar_stock_desde_github(carro):
    response = requests.get(GITHUB_RAW_URL)
    if response.status_code == 200:
        data = response.json()
        for producto in data['products']:
            try:
                # Obtener el producto actual de la base de datos
                producto_bd = Product.objects.get(id=producto['id'])
                # Obtener la cantidad comprada de ese producto del carrito
                if str(producto_bd.id) in carro.carro:
                    cantidad_comprada = carro.carro[str(producto_bd.id)]['cantidad']
                    # Actualizar el stock en la base de datos restando la cantidad comprada
                    producto_bd.stock -= cantidad_comprada
                    producto_bd.save()
            except Product.DoesNotExist:
                print(f"Producto con id {producto['id']} no existe.")
    else:
        print("Error al cargar el archivo JSON desde GitHub")


def procesar_compra(request):
    carro = Carro(request)
    productos_no_disponibles = []

    # Crear un nuevo objeto Carrito en la base de datos
    nuevo_carrito = Carrito()
    nuevo_carrito.fecha_compra = timezone.now()
    nuevo_carrito.cantidad_total = carro.cantidad_total_productos()
    nuevo_carrito.save()

    for key, item in list(carro.carro.items()):
        try:
            producto = Product.objects.get(id=item['producto_id'])
            if producto.stock >= item['cantidad']:
                producto.stock -= item['cantidad']
                producto.save()
                # Añadir productos al nuevo carrito
                nuevo_carrito.productos.add(producto)
            else:
                messages.error(request, f"No hay suficiente stock para {producto.nombre_producto}.")
                return redirect('ver_carro')
        except Product.DoesNotExist:
            nombre_producto = item.get('nombre', 'Producto desconocido')
            productos_no_disponibles.append(nombre_producto)
            del carro.carro[key]  # Eliminar producto inexistente del carrito

    if productos_no_disponibles:
        messages.error(request, f"Los siguientes productos ya no están disponibles: {', '.join(productos_no_disponibles)}")
        return redirect('ver_carro')

    nuevo_carrito.save()
    carro.limpiar_carro()
    cargar_stock_desde_github(carro)  # Llamar a la función para actualizar el stock
    messages.success(request, 'Gracias por su compra!')
    return redirect('index')