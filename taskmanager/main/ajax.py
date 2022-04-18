from .models import *
from django.db.models import *
from django.http import HttpResponse, JsonResponse
from django.views import View
from .forms import *


class addBacket(View):

    def post(self, request):
        if not updateBacket().post(request):
            user_id = int(request.session['user_id'])
            product_id = request.POST.get('productId')

            newOrder = backetForm()
            newOrder.user = User.objects.get(pk=user_id)
            newOrder.product = products.objects.get(pk=product_id)
            newOrder.quantity = 1
            newOrder.save()

        return HttpResponse(200)


class updateBacket(View):

    def post(self, request):
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

        print(request.POST.get('update'))

        if request.POST.get('update'):
            return HttpResponse(200)
        else:
            return result


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
