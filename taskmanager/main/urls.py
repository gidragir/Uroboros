from django.urls import path, re_path
from . import  views, ajax

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('registration', views.registration, name='registration'),
    path('authorization', views.authorization, name='authorization'),
    path('backet', views.backetOfUser, name='backet'),
    path('backetOperation',
         ajax.backetOperation.as_view(), name='backetOperation'),
        re_path('backetOperation/<int:backet_id>',
                ajax.backetOperation.as_view()),
    path('productMore', ajax.productMore.as_view(), name='productMore'),
    path('sellProduct', views.sellProduct, name='sellProduct')
]
