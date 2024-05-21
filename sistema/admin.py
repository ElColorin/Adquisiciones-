from django.contrib import admin
from .models import Category
from .models import Product
from .models import Post


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

