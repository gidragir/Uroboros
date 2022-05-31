import base64
from email import header
import json
from django.http import HttpResponse
import requests
from .models import *
from django.db.models import *


class functions:
   
  def requestSerialization(data):
       
    items = data.items()
        
    serialization = {}
    
    for item in items:
      serialization[item[0]] = item[1]

    return serialization
  
  def updateBacket(request):
    user_id = request.session['user_id']
    product_id = request.POST.get('productId')
    quantity = request.POST.get('quantity')

    backetStorage = backet.objects.filter(
         user_id=user_id, product_id=product_id)

    if backetStorage.count() > 0:
        backetStorage.update(quantity=F('quantity') + quantity)
        result = True
    else:
        result = False

    if request.POST.get('update'):
        return HttpResponse(200)
    else:
        return result
      
  def makeOrder(request):
    
    # backet_ids = request.POST.getlist("backet_ids[]")
    # for backet_id in backet_ids:
    #   print(backet_id)

    user_id = request.POST.get("user_id")
    product_ids = backet.objects.filter(user_id=user_id)
  
    mass = []
    for item in product_ids.values("product_id", "quantity"):
      info = {
          "product_id": item["product_id"],
          "quantity": item["quantity"],
      }
      mass.append(info)
    product_ids.delete()
    headers = urlFunc.collHeaders({}, True)
    data = {
        "backet": mass
    }
    
    result = HttpResponse(urlFunc.sendRequest("post", "sell", headers, data))
    
    return result

class urlFunc:
  
  def methodUrl(name):
    return "http://localhost/Django/hs/base/" + name

  def collHeaders(headers, autho=False):
        
    if autho:
      headers['Authorization'] = urlFunc.base64Autho()    
    return headers      

  def sendRequest(method, urlName, headers, data):
    url = urlFunc.methodUrl(urlName)
    json_data = json.dumps(data)
    res = exec("requests." + method + "(url, headers=headers, data=json_data)")
    return res
  
  def base64Autho():
    strBytes = str(base64.b64encode(
      'Администратор:147596'.encode()))[2:]
    Authorization = 'Basic ' + strBytes
    return Authorization
