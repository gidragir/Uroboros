from .forms import regForm
from itertools import product
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import connection
connection.queries
from django.db.models import *
from .models import products, productmove
from . import code

# Create your views here.


def index(request):
    sessionData = code.functions.requestSerialization(request.session)
        
    allproducts = products.objects.values('id', 'name').annotate(quantity=Sum('productmove__quantity'))
    sessionData['allproducts'] = allproducts

    return render(request, 'main/index.html', sessionData)

def about(request):
    sessionData = code.functions.requestSerialization(request.session)
    
    return render(request, 'main/about.html', sessionData)

def registration(request):
    
    sessionData = code.functions.requestSerialization(request.session)
    Form = regForm()

    if request.method == "POST":
        
        print(request.POST.get("username") +
              request.POST.get("first_name") + request.POST.get("last_name"))
        
        return render(request, 'main/index.html', sessionData)
    else:
        
        sessionData['regForm'] = Form
        return render(request, 'main/registration.html', sessionData)

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
