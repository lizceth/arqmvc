"""arqmvc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.conf import settings
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'app.views.inicio', name='inicio'),
    url(r'^app/$', 'app.views.inicio'),
    url(r'^clienteList/$', 'app.views.ClienteInfo'),
    url(r'^clienteAdd/$', 'app.views.Cliente_add'),
    url(r'^clienteEdit/(?P<id>\d+)$', 'app.views.Cliente_edit'),
    url(r'^clienteBorrar/(?P<id>\d+)$', 'app.views.Cliente_borrar'),
    url(r'^pedidoList/$', 'app.views.PedidoInfo'),
    url(r'^pedidoAdd/$', 'app.views.Pedido_add'),
    url(r'^app/', include('app.urls')),




]
