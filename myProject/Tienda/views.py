from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .forms import Cliente_form,Carrito_form
from .models import Cliente,Inventario,Carrito
from django.db.models import Q
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView
from  django.urls import reverse_lazy
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
        self.object = Inventario.objects.get(id_inventario=pk)
        self.data = {'cantidad_producto':1,
                     'cliente_id': 1 ,
                     'inventario_id':self.object.id_inventario,
                     'precio_unidad':self.object.precio_producto}
        print(type(self.data))
        f = Carrito_form(self.data)
        f.save()
        self.template_name = 'Tienda/detalle.html'
        return render(request,self.template_name,{'data':self.data})

    #def post(self, request,*args, **kwargs):

        # form = self.form_class(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return HttpResponseRedirect(self.success_url)
        # else:
        #     print(form.errors)
        # return super(Detalle_producto, self).post(request,*args, **kwargs)


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