from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('registration', views.registration, name='registration'),
    path('authorization', views.authorization, name='authorization'),
    path('backet', views.backetOfUser, name='backet'),
    path('addBacket', views.addBacket.as_view(), name='addBacket'),
    path('updateBacket', views.updateBacket.as_view(), name='updateBacket'),
    path('productMore', views.productMore.as_view(), name='productMore'),
    path('sellProduct', views.sellProduct, name='sellProduct')
]
