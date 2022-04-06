from datetime import datetime
from distutils.log import error
from django.contrib.auth import authenticate
from .forms import *
from itertools import product
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.db import connection
connection.queries
from django.db.models import *
from .models import products, productmove
from . import code

# Create your views here.


def index(request):
    if request.GET.get('delete'):
        del request.session['user_id']
        del request.session['user_name']

    sessionData = code.functions.requestSerialization(request.session)
        
    allproducts = products.objects.values('id', 'name').annotate(quantity=Sum('productmove__quantity'))
    sessionData['allproducts'] = allproducts
    Form = authoForm()
    sessionData['authoForm'] = Form

    return render(request, 'main/index.html', sessionData)

def about(request):
    if request.GET.get('delete'):
        del request.session['user_id']
        del request.session['user_name']

    sessionData = code.functions.requestSerialization(request.session)
    Form = authoForm()
    sessionData['authoForm'] = Form
    
    return render(request, 'main/about.html', sessionData)

def registration(request):
    
    sessionData = code.functions.requestSerialization(request.session)
    if request.method == "POST":

        Form = regForm(request.POST)
        
        if Form.is_valid():
            user = Form.save()
            request.session['user_id'] = user.id
            request.session['user_name'] = user.username
            return redirect('home')
    else:
        Form = regForm()
        
    sessionData['regForm'] = Form
    return render(request, 'main/registration.html', sessionData)

def authorization(request):
    sessionData = code.functions.requestSerialization(request.session)
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    errorMessages = {}
    sessionData['errorMessages'] = errorMessages
    
    if request.method == "POST":

        user = authenticate(username=username, password=password)
        if user is not None:
            user.last_login = datetime.now()
            user.save()
            request.session['user_id'] = user.id
            request.session['user_name'] = user.username
            
            return redirect('home')
        else:     
            usernameCheck = User.objects.filter(username=username)
            if usernameCheck:
                passwordCheck = usernameCheck.filter(password=username)
                if not passwordCheck:
                    errorMessages['passwordError'] = "Не правильный пароль"
            else:
                errorMessages['loginError'] = "Не правильный логин"
            sessionData['errorMessages'] = errorMessages
    Form = authoForm()
    sessionData['authoForm'] = Form
    return render(request, 'main/authorization.html', sessionData)

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
