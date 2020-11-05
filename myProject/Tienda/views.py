from django.shortcuts import render,HttpResponse

# Create your views here.

def login(request):
    return render(request,'Tienda/login.html')

def registrar(request):
    return render(request,'Tienda/register.html')