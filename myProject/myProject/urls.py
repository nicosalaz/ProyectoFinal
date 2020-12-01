"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from Usuario.views import Login,logout_usuario
from Tienda.views import Index,Index_login,Detalle_producto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Tienda/',include(('Tienda.urls','Tienda'))),
    path('Indexlog/',Index_login.as_view(),name='Index_login'),
    path('Index/',login_required(Index.as_view()),name='Index'),
    path('accounts/login/',Login.as_view(),name= 'login'),
    path('logout/',login_required(logout_usuario),name='logout'),
    path('detalle/<int:pk>/',login_required(Detalle_producto.as_view()),name='detalle'),
]
