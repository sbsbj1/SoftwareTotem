from django.urls import path 
from .views import home, ver, mostrar, form_cliente, form_modcliente, form_del_cliente

urlpatterns = [ 
    path('', home, name="home"),
    path('ver/', ver, name="ver"),
    path('mostrar/', mostrar, name="mostrar"),
    path('form_cliente/', form_cliente, name="form_cliente"), 
    path('form_modcliente/<id>', form_modcliente, name="form_modcliente"),
    path('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente")

] 