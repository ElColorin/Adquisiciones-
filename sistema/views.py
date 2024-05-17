from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'sistema/index.html', {'categories': categories, 'products': products})

def filter_products(request):
    category_id = request.GET.get('category_id')
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    products_data = [{
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'image_url': product.image.url,
        'category': product.category.name,
    } for product in products]

    return JsonResponse({'products': products_data})
