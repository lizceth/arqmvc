from django.forms import ModelForm
from django import forms
from app.models import Cliente, Pedido

class ClienteForm(ModelForm):
     class Meta:
         model = Cliente
         #fields = ("nombres", "telefono")

class PedidoForm(ModelForm):
     class Meta:
         model = Pedido
         #fields = ("descripcion", "fecha", "cliente")