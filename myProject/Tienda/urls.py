from django.urls import path
from .views import *
urlpatterns=[
    path('login/',login,name='login'),
    path('registrar/',registrar,name='registrar'),

]