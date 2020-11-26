from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
urlpatterns=[
    path('Registrar/',Registrar.as_view(),name='Registrar'),
    path('Carrito/',agregar_carrito.as_view(), name='Carrito'),
]