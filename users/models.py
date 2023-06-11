from django.contrib.auth.models import AbstractUser
from django.db import models

from common.constants import Role
from origindb.models import Inprodtype
from users.managers import UserManager


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(choices=Role.ROLE_CHOICES, default=Role.WORKER, max_length=55)

    objects = UserManager()

    def __str__(self):
        return self.get_full_name()


class CategoryAccess(models.Model):
    """
        Using for manager access to categories
            - need change column recno5 (table inprodtype) to unique
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='category_access')
    category = models.ForeignKey(
        Inprodtype, to_field="recno5", on_delete=models.CASCADE, blank=True, null=True, related_name='category_access'
    )
