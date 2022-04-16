from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('registration', views.registration, name='registration'),
    path('authorization', views.authorization, name='authorization'),
    path('backet', views.backet, name='backet'),
    path('addBacket', views.addBacket, name='addBacket'),
    path('productMore', views.productMore, name='productMore'),
    path('sellProduct', views.sellProduct, name='sellProduct')
]
