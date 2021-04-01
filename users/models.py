from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from .managers import CustomUserManger


# Create your models here.

class CustomUser(AbstractUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    username = None
    first_name = None
    last_name = None
    date_joined = None
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManger()