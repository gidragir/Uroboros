from .models import *
from django.db.models import *
from django.http import HttpResponse, JsonResponse
from django.views import View
from .forms import *
from .code import functions


class backetOperation(View):
    
    def post(self, request): 
        operation = request.POST.get('operation')

        if operation == "add":
            if not functions.updateBacket(self, request):
                user_id = int(request.session['user_id'])
                product_id = request.POST.get('productId')

                newOrder = backetForm()
                newOrder.user = User.objects.get(pk=user_id)
                newOrder.product = products.objects.get(pk=product_id)
                newOrder.quantity = 1
                newOrder.save()
                
        elif operation == "update":
            functions.updateBacket(request)
        
        elif operation == "makeOrder":
            functions.makeOrder(request)
            
        return HttpResponse(200)
    
    def delete(self, request, backet_id):
        
        backet.objects.filter(pk=backet_id).delete()
        
        return HttpResponse(200)
class productMore(View):

    def get(self, request):
        productId = request.GET.get('productId')
        productData = products.objects.filter(pk=productId).annotate(
            quantity=Sum('productmove__quantity')).get(pk=productId)

        if productData.quantity == None:
            quantity = 0
        else:
            quantity = productData.quantity

        json = {
            'name': productData.name,
            'description': productData.description,
            'quantity': quantity,
            'price': productData.price,
            'picture': productData.picture
        }

        return JsonResponse(json)
