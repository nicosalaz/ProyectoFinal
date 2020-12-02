from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .forms import Cliente_form,Carrito_form
from .models import Cliente,Inventario,Carrito
from django.db.models import Q
from django.views.generic import DeleteView,CreateView,ListView,DetailView,UpdateView
from  django.urls import reverse_lazy
from django.db.models import Sum
# Create your views here.

class Index(ListView,CreateView):
    model = Inventario
    form_class = Carrito_form
    template_name = 'Tienda/index.html'
    success_url = reverse_lazy('Index')
    queryset = Inventario.objects.filter(cantidad__gt=0)

    def get(self, request, *args, **kwargs):
        queryset = request.GET.get("buscar")
        object_list = Inventario.objects.filter(cantidad__gt = 0)
        if queryset:
            object_list = Inventario.objects.filter(
                Q(categoria_id__nombre__icontains=queryset) |
                Q(persona_id__nombre__icontains=queryset),
                categoria_id__gt=0
            ).distinct()
        return render(request,self.template_name,{'object_list':object_list})
    
    # def get_context_data(self, **kwargs):
    #     context = super(Index, self).get_context_data()
    #     if 'formu' not in context:
    #         context['formu'] = self.form_class(self.request.GET)
    #     return context
    #
    #
    # def post(self, request,*args, **kwargs):
    #     self.model = Carrito
    #     formu = self.form_class(request.POST)
    #     if formu.is_valid():
    #         solicitud = formu.save()
    #         solicitud.save()
    #         return HttpResponseRedirect(self.success_url)
    #     return super(Index, self).post(request,*args, **kwargs)

class Detalle_producto(CreateView,DetailView):
    model = Carrito
    form_class = Carrito_form
    data = 0
    template_name = 'Tienda/detalle.html'
    success_url = reverse_lazy('Index')
    def get(self, request, pk,*args, **kwargs):
        self.model = Inventario
        self.template_name = 'Tienda/detalle.html'
        self.object = Inventario.objects.get(id_inventario=pk)
        self.data = {'cantidad_producto':1,
                     'cliente_id': 1 ,
                     'inventario_id':self.object.id_inventario,
                     'precio_unidad':self.object.precio_producto}
        print(type(self.data))
        f = Carrito_form(self.data)
        f.save()
        self.object.cantidad = self.object.cantidad - 1
        self.object.save()
        return render(request,self.template_name,{'object':self.object})


class Registrar(CreateView):
    model = Cliente
    form_class = Cliente_form
    template_name = 'Tienda/register.html'
    success_url = reverse_lazy('login')

class Index_login(ListView):
    model = Inventario
    template_name = 'Tienda/indexLogin.html'
    queryset = Inventario.objects.filter(cantidad__gt=0)

    def get(self, request, *args, **kwargs):
        queryset = request.GET.get("buscar")
        object_list = Inventario.objects.filter(cantidad__gt = 0)
        if queryset:
            object_list = Inventario.objects.filter(
                Q(categoria_id__nombre__icontains = queryset) |
                Q(persona_id__nombre__icontains = queryset),
                categoria_id__gt=0
            ).distinct()
        return render(request,self.template_name,{'object_list':object_list})

class Carrito_compra(ListView):
    model = Carrito
    template_name = 'Tienda/carrito_compra.html'
    queryset = Carrito.objects.filter(estado = True)


class Eliminado(DeleteView):
    model = Carrito
    success_url = ('Tienda/carrito_confirm_delete.html')

    def get(self, request, pk,*args, **kwargs):
        self.object = Carrito.objects.get(id_carrito=pk)
        self.object_dos = Carrito.objects.filter(estado=True).aggregate(Sum('precio_unidad'))
        self.template_name = 'Tienda/carrito_confirm_delete.html'
        self.data = {'inventario_id_pro': self.object.inventario_id.persona_id,
                     'precio_unidad': self.object.precio_unidad,
                     'inventario_id' : self.object.inventario_id.id_inventario
                     }
        obj_dos = Inventario.objects.get(id_inventario=self.data.get('inventario_id'))
        self.object.estado = False
        self.object.save()
        obj_dos.cantidad = obj_dos.cantidad + 1
        obj_dos.save()
        return render(request,self.template_name,{'data':self.data})



class Factura(DeleteView):
    model = Carrito
    success_url = ('Tienda/factura.html')

    def get(self, request,*args, **kwargs):
        self.object = Carrito.objects.filter(estado = True).aggregate(Sum('precio_unidad'))
        self.dato = Carrito.objects.all().update(estado=False)
        self.template_name = 'Tienda/factura.html'
        return render(request,self.template_name,{'object':self.object})