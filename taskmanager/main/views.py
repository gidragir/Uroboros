from itertools import product
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import connection
connection.queries
from django.db.models import *
from .models import products, productmove

# Create your views here.


def index(request):
    # allproducts = productmove.objects.values('product__name', 'product').annotate(quantity= Sum('quantity'))
    allproducts = products.objects.values('id', 'name').annotate(quantity=Sum('productmove__quantity'))
    request.session['test1'] = 'test1'
    return render(request, 'main/index.html', {'allproducts': allproducts})


def about(request):
    return render(request, 'main/about.html')

def productMore(request):
    productId = request.GET.get('productId')
    productData = products.objects.filter(pk=productId).annotate(quantity=Sum('productmove__quantity')).get(pk=productId)
    
    if productData.quantity == None:
        quantity = 0
    else:
        quantity = productData.quantity
        
    json = {
       'name': productData.name,
       'description': productData.description,
       'quantity': quantity     
    }
    
    return JsonResponse(json)
