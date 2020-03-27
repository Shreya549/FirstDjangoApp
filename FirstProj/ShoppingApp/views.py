from django.shortcuts import render, redirect
from .models import Product
# Create your views here.
def index(request):
    prod1 = Product()
    prod1.name = 'Hat'
    prod1.price = 5
    prod1.desc = 'A beach hat'
    prod1.img = 'product_02.jpg'

    prod2 = Product()
    prod2.name = 'Muffler'
    prod2.price = 10.2
    prod2.desc = 'Protects you from the cold winds'
    prod2.img = 'product_03.jpg'

    prod3 = Product()
    prod3.name = 'Shoes'
    prod3.price = 20.52
    prod3.desc = 'The best you can wear'
    prod3.img = 'product_01.jpg'

    prods = [prod1, prod2, prod3]
    return render(request, 'index.html', {'prods' : prods})