from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from my_boilerplate_django_admin.core.mixins import BaseModel


class User(AbstractUser):
    """Default user for My Boilerplate Django Admin."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Papeis(BaseModel):
    titulo = models.CharField(
        "Título",
        max_length=20,
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Papel"
        verbose_name_plural = "Papéis"
        ordering = [
            "titulo",
        ]
