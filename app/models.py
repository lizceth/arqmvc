from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    def __str__(self):
        return str(self.nombres)

class Pedido(models.Model):
    """docstring for Pedido"""
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente)

    def __str__(self):
        return str(self.cliente)

class Atencion(models.Model):

    """docstring for Atencion"""
    fecha = models.DateField(auto_now_add=True)
    Pedido = models.ForeignKey(Pedido)
    doctor = models.ForeignKey(User)
    tratamiento = models.TextField()

    def __str__(self):
        return str(self.pedido.cliente.nombres)