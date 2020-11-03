from django.shortcuts import render,HttpResponse

# Create your views here.

def login(request):
    return render(request,'Tienda/index.html')

def tienda(request):
    return HttpResponse("tienda")