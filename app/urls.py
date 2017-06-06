from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from .views import ClienteProxyViewSet
#router = ExtendedSimpleRouter()
router = routers.DefaultRouter()

router.register(r'cliproxies', ClienteProxyViewSet)

urlpatterns = [

    url(r'^cliproxy/$', ClienteProxyViewSet),

    url(r'^', include(router.urls)),
]
