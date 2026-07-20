from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model for Taikisha Industrial Platform.
    """

    employee_id = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    roles = models.ManyToManyField(
        "rbac.Role",
        blank=True,
        related_name="users",
    )


    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"


    def __str__(self):

        return self.username