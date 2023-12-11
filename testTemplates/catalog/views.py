from django.shortcuts import render
from .models import Product

MENU = {"Главная":"/", "Страница постов":"/catalog", "О блоге":"/about"}



def catalog_page(request):
    products = Product.objects.all()
    title = "Страница постов"
    data = {"menu" :MENU, "title": title, "products": products}
    return render(request, './catalog.html', context=data)