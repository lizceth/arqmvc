from __future__ import unicode_literals

from django.db import models
from .PersonManager import ClienteManager
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
<<<<<<< HEAD
        return str(self.pedido.cliente.nombres)
=======
        return "%s - %s " % (self.fecha, self.pedido.cliente)
    
class ClienteProxy(Cliente):
    objects = ClienteManager()
    class Meta:
        proxy = True
>>>>>>> 0dd68e531acfbbf2d418c50ebb0e9ac6a41899bf
