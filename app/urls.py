from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from .views import ClienteViewSet, PedidoViewSet, AtencionViewSet
#router = ExtendedSimpleRouter()
router = routers.DefaultRouter()

router.register(r'clientes', ClienteViewSet)

router.register(r'pedidos', PedidoViewSet)

router.register(r'atenciones', AtencionViewSet)

urlpatterns = [

    url(r'^cliente/$', ClienteViewSet),

    url(r'^pedido/$', PedidoViewSet),

    url(r'^atencion/$', AtencionViewSet),

    url(r'^', include(router.urls)),
]
