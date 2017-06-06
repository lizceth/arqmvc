from django.contrib import admin

from app.models import Cliente, Pedido, Atencion, ClienteProxy


admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Atencion)
admin.site.register(ClienteProxy)