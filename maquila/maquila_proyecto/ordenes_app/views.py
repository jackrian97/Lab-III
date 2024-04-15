from django.shortcuts import render
# Importamos las vistas generaicas para el CRUD
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import OrdenPedido, ListaPares
# Create your views here.

class OrdenPedidoListado(ListView):
    model = OrdenPedido, ListaPares

class OrdenPedidoCrear(CreateView):
    model = OrdenPedido
    fields = ['orden_pedido', 'bloque', 'fecha_orden', 'fecha_entrega', 'cliente', 'referencia', 'foto_orden']
    template_name = 'crear.html'

    def form_valid(self, form):
        # Guarda el formulario de OrdenPedido antes de procesar los datos de ListaPares
        orden_pedido = form.save(commit=False)
        orden_pedido.save()

        # Obtén los datos del formulario de ListaPares y asígnalos al objeto de OrdenPedido recién creado
        lista_pares_data = self.request.POST.getlist('talla')
        for talla in lista_pares_data:
            lista_pares = ListaPares(orden_pedido=orden_pedido, talla=talla)
            lista_pares.save()

        return super().form_valid(form)
    
