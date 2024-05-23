from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category

def index(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
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
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'image_url': product.image.url,
        'category': product.categoria.name,
    } for product in products]

    return JsonResponse({'products': products_data})