from django.contrib import admin
from .models import *


# Register your models here.
class productsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    
admin.site.register(products, productsAdmin)

class productmoveAdmin(admin.ModelAdmin):
    list_display = ['date','product', 'quantity']
    list_filter = ['date', 'product']
 
admin.site.register(productmove, productmoveAdmin)
