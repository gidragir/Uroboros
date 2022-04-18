import base64
import requests
from .code import functions
from .models import products
from django.db.models import *
from datetime import datetime
from distutils.log import error
import re
from django.contrib.auth import authenticate
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .ajax import *
# Create your views here.


def index(request):

    request.session.set_expiry(0)

    if request.GET.get('delete'):
        del request.session['user_id']
        del request.session['user_name']

    if request.POST.get('productId'):
        addBacket(request)

    sessionData = functions.requestSerialization(request.session)

    allproducts = products.objects.values('id', 'name', 'price', 'picture')
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


def backetOfUser(request):

    sessionData = functions.requestSerialization(request.session)
    user = User.objects.get(pk=sessionData['user_id'])
    products = backet.objects.filter(user=user).values(
        'id', 'product', 'product__name', 'quantity', 'product__price', 'product__picture')
    sessionData['products'] = products

    return render(request, 'backet/index.html', sessionData)

def sellProduct(request):

    strBytes = str(base64.b64encode(
        'Администратор:147596'.encode()))[2:]
    Authorization = 'Basic ' + strBytes
    headers = {'Authorization': Authorization}

    res = requests.post(
        'http://localhost/Django/hs/base/sell', headers=headers)

    return HttpResponse(res)
