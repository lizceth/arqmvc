from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Cliente, Pedido, ClienteProxy
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from app.forms import ClienteForm, PedidoForm
from django.utils import timezone
from rest_framework import serializers, viewsets

def inicio(request):
    pedidos = Pedido.objects.order_by('fecha')
    return render_to_response('base.html', {'pedidos': pedidos},
                              context_instance=RequestContext(request))

def ClienteInfo(request):
    clientes = ClienteProxy.objects.all()
    titulo = "pagina  de  clientes "
    return render_to_response('app/cliente.html', {
        'clientes': clientes, 'titulo': titulo},
         context_instance=RequestContext(request))

def Cliente_add(request):
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/clienteList/')
    else:
        formulario = ClienteForm()
    return render_to_response('app/clienteAdd.html',
                              {'formulario': formulario},
                          context_instance=RequestContext(request))


def Cliente_edit (request, id):
        cliente_edit= Cliente.objects.get(pk=id)
        if request.method == 'POST':
            formulario = ClienteForm(request.POST, instance=cliente_edit)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/clienteList/")
        else:
            formulario = ClienteForm(instance=cliente_edit)
        return render_to_response('app/clienteEdit.html',
                                 {'formulario': formulario},
                                  context_instance=RequestContext(request))
def Cliente_borrar (request, id):
    cliente_borrar = get_object_or_404(Cliente, pk=id)
    cliente_borrar.delete()
    return HttpResponseRedirect("/clienteList/")


def PedidoInfo(request):
    pedidos = Pedido.objects.order_by('fecha')
    titulo = "pagina  de  pedidos "
    return render_to_response('app/pedido.html', {
        'pedidos': pedidos, 'titulo': titulo},
         context_instance=RequestContext(request))

def Pedido_add(request):
    if request.method == 'POST':
        formulario = PedidoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/pedidoList/')
    else:
        formulario = PedidoForm()
    return render_to_response('app/pedidoAdd.html',
                              {'formulario': formulario},
                          context_instance=RequestContext(request))

class ClienteProxySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteProxy
        fields = '__all__'

class ClienteProxyViewSet(viewsets.ModelViewSet):
    queryset = ClienteProxy.objects.all()
    serializer_class = ClienteProxySerializer