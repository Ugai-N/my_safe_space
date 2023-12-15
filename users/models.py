from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.CharField(verbose_name='email', unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    is_client = models.BooleanField(_("client"), default=True)
    avatar = models.ImageField(verbose_name='аватар', upload_to='users/', **NULLABLE)
    telegram = models.CharField(verbose_name='telegram_id', unique=True)
    phone = models.CharField(verbose_name='телефон', max_length=35, **NULLABLE)
    city = models.CharField(verbose_name='город', max_length=50, **NULLABLE)
