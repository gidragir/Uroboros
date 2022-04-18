from django.urls import path
from . import  views, ajax

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('registration', views.registration, name='registration'),
    path('authorization', views.authorization, name='authorization'),
    path('backet', views.backetOfUser, name='backet'),
    path('addBacket', ajax.addBacket.as_view(), name='addBacket'),
    path('updateBacket', ajax.updateBacket.as_view(), name='updateBacket'),
    path('productMore', ajax.productMore.as_view(), name='productMore'),
    path('sellProduct', views.sellProduct, name='sellProduct')
]
