from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Product, Category, CustomAuthenticationForm, Carrito
from .carro import Carro
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
import requests
from django.utils import timezone
import json

PROVIDERS_API_URL = 'https://qic534o8o0.execute-api.us-east-1.amazonaws.com/proveedor/productos'
PROVIDERS_CATEGORIES_API_URL = 'https://qic534o8o0.execute-api.us-east-1.amazonaws.com/proveedor/categorias'
API_KEY = 'ywtS9pGyNp8ndqyW3nLoj8mANCUd8cxO8irRwD4s'

def index(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    
    headers = {
        'x-api-key': API_KEY,
    }
    
    try:
        response = requests.get(PROVIDERS_API_URL, headers=headers)
        response.raise_for_status()
        productos = response.json()
        
        # Obtener categorías
        categories_response = requests.get(PROVIDERS_CATEGORIES_API_URL, headers=headers)
        categories_response.raise_for_status()
        categories = categories_response.json()
        
        # Filtrar productos por búsqueda
        if query:
            productos = [producto for producto in productos if query.lower() in producto['nombre_producto'].lower()]
        
        # Filtrar productos por categoría
        if category_id:
            productos = [producto for producto in productos if str(producto['categoria_id_categoria']) == category_id]
        
        data = {
            'products': productos,
            'categories': categories,
            'query': query,
            'selected_category': category_id,
        }
        return render(request, 'sistema/index.html', data)
    
    except requests.RequestException as e:
        print(f"Error al obtener los productos de la API de proveedores: {e}")
        messages.error(request, 'Error al obtener los productos de la API de proveedores.')
        return render(request, 'sistema/index.html', {'products': [], 'categories': [], 'query': query, 'selected_category': category_id})
    

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
    headers = {
        'x-api-key': API_KEY,
    }
    
    try:
        response = requests.get(f'{PROVIDERS_API_URL}/{product_id}', headers=headers)
        response.raise_for_status()
        producto = response.json()
        
        # Imprimir la respuesta de la API para verificar su estructura
        print(json.dumps(producto, indent=4))
        
        # Crear una instancia del carrito y agregar el producto
        carro = Carro(request)
        carro.agregar(producto)
        messages.success(request, f'{producto["nombre_producto"]} ha sido agregado al carrito.')
    except requests.RequestException as e:
        print(f"Error al obtener el producto de la API de proveedores: {e}")
        messages.error(request, 'Error al agregar el producto al carrito.')
    
    return redirect('index')


def ver_carro(request):
    carro = Carro(request)
    return render(request, 'sistema/carrito.html', {'carro': carro})

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    print('error_carrito')
    headers = {
        'x-api-key': API_KEY,
    }
    
    try:
        response = requests.get(f'{PROVIDERS_API_URL}/{producto_id}', headers=headers)
        response.raise_for_status()
        producto = response.json()
        carro.eliminar(producto)
        print('carro')
        messages.success(request, f'{producto['nombre_producto']} ha sido eliminado del carrito.')
        print('try')
    except Product.DoesNotExist:
        print('except')
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
        print('xd')
        username = request.POST.get('username')
        password = request.POST.get('password')
        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZHF1aXNpY2lvbmVzIjoidG9rZW5fYWRxdWlzaWNpb25lcyJ9.8cKAY45kC9w9gJAp2a_h99A4RZJEuFcExBcoVfwZIc0'
        
        # Datos para la solicitud POST
        payload = json.dumps({
            "username": username,
            "password": password,
            "token": token
        })
        
        headers = {
            'Content-Type': 'application/json'
        }

        # URL del endpoint de validación
        url = 'https://qic534o8o0.execute-api.us-east-1.amazonaws.com/validacionUsuarios/'
        
        try:
            # Realizar la solicitud POST
            response = requests.post(url, headers=headers, data=payload)
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.content}")
            
            if response.status_code == 200:
                print("Resultado Exitoso")
                result = response.json()
                print(f"Result: {result}")
                if result.get('valid', False):
                    # Autenticar al usuario en Django
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, 'Inicio de sesión exitoso')
                        return redirect('index')
                    else:
                        messages.error(request, 'No se pudo autenticar al usuario en el sistema local')
                else:
                    messages.error(request, 'Credenciales inválidas')
            else:
                messages.error(request, 'Error en la validación de usuario')
        
        except Exception as e:
            print(f"Exception occurred: {e}")
            messages.error(request, 'Ocurrió un error durante la solicitud de validación')
        return redirect('index')
    else:
        return render(request, 'Sistema/login.html')

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