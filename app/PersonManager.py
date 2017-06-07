from django.db import models
from django.db.models import Q
from django.conf import settings
# from django.contrib.auth.models import UserManager

class ClienteManager(models.Manager):  # models.Manager

    """ """

    def get_queryset(self):
        return super(ClienteManager, self).get_queryset()