from django.urls import path
from .views import *
urlpatterns=[
    path('',login,name='Login'),
    path('',registrar,name='Registrar'),

]