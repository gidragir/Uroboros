from django.http import HttpResponse
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
    
    backet_ids = request.POST.getlist("backet_ids[]")
    for backet_id in backet_ids:
      print(backet_id)
    
    return HttpResponse(200)
