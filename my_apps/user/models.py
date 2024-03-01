from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy

from my_apps.user.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=120,
        unique=True,
        verbose_name=gettext_lazy("Email address")
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name=gettext_lazy("First name")
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=gettext_lazy("Last name")
    )
    username = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=75,
        blank=True,
        null=True
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='my_apps_user_set'  # change the related_name value
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='my_apps_user_set'  # change the related_name value
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

