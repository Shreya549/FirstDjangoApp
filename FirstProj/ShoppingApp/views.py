from django.shortcuts import render, redirect
from .models import Product
# Create your views here.
def index(request):
    
    prods = Product.objects.all()
    return render(request, 'index.html', {'prods' : prods})