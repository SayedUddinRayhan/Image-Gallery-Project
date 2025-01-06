from django.http import HttpResponse
from django.shortcuts import render

from gallery.models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'index/index.html', {'prod': products})

def home(request):
    return render(request, 'index/home.html')