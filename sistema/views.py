from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Product, Category, CustomAuthenticationForm
from .carro import Carro
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


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
    producto = get_object_or_404(Product, id=producto_id)
    if producto:
        carro.eliminar(producto)
    return redirect('ver_carro')

def restar_producto(request, producto_id):
    producto = get_object_or_404(Product, pk=producto_id)
    carro = Carro(request)
    carro.restar(producto)
    return redirect('ver_carrito')

def procesar_compra(request):
    carro = Carro(request)
    carro.limpiar_carro()
    messages.success(request, 'Gracias por su Compra!!')
    return render(request, 'sistema/procesar_compra.html')



def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido {username}!')
                return redirect('index')  # Redirige a la página principal de productos después del login
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = CustomAuthenticationForm()  # Utiliza el formulario personalizado
    return render(request, 'sistema/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente')
    return redirect('index')  # Redirige a la página principal de productos después del logout