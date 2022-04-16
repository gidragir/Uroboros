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
from .code import functions
import requests
import base64

# Create your views here.


def index(request):
    
    request.session.set_expiry(0)
    
    if request.GET.get('delete'):
        del request.session['user_id']
        del request.session['user_name']
    
    sessionData = functions.requestSerialization(request.session)
        
    allproducts = products.objects.values('id', 'name').annotate(quantity=Sum('productmove__quantity'))
    sessionData['allproducts'] = allproducts
    Form = authoForm()
    sessionData['authoForm'] = Form

    return render(request, 'main/index.html', sessionData)

def about(request):
    if request.GET.get('delete'):
        del request.session['user_id']
        del request.session['user_name']

    sessionData = functions.requestSerialization(request.session)
    Form = authoForm()
    sessionData['authoForm'] = Form
    
    return render(request, 'main/about.html', sessionData)

def registration(request):
    
    sessionData = functions.requestSerialization(request.session)
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
    sessionData = functions.requestSerialization(request.session)
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

def backet(request):

    if request.GET.get('delete'):
        del request.session['user_id']
        del request.session['user_name']
        
    sessionData = functions.requestSerialization(request.session)

    return render(request, 'backet/index.html', sessionData)


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

def sellProduct(request):
    
    strBytes = str(base64.b64encode(
        'Администратор:147596'.encode()))[2:]
    Authorization = 'Basic ' + strBytes
    headers = {'Authorization': Authorization}
    
    res = requests.post('http://localhost/Django/hs/base/sell', headers=headers)
    
    return HttpResponse(res)
