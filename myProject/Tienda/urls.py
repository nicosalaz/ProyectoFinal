from django.urls import path
from .views import *
urlpatterns=[
    path('Registrar/',Registrar.as_view(),name='Registrar'),
    path('',Index.as_view(),name='Index'),
]