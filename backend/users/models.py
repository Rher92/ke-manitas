from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models

from backend.utils.models import BaseCreatedUpdatedModel

class User(AbstractUser):
    """
    Default custom user model for backend.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

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


class Cliente(BaseCreatedUpdatedModel):
    user = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
        )
    ciudad = models.CharField(blank=True, null=True, max_length=255)
    barrio = models.CharField(blank=True, null=True, max_length=255)
    casa = models.CharField(blank=True, null=True, max_length=255)
    nombre = models.CharField(blank=True, null=True, max_length=255)
    tipo_de_documento = models.CharField(blank=True, null=True, max_length=255)
    documento = models.CharField(blank=True, null=True, max_length=255)
    barrio = models.CharField(blank=True, null=True, max_length=255)
    telefono = models.IntegerField(blank=True, null=True, max_length=30)
    email = models.EmailField(blank=True, null=True, max_length=100)

    def __str__(self) -> str:
        return f'{self.user.name}'

class Prestamos(BaseCreatedUpdatedModel):
    user = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
        )
    cantidad = models.IntegerField(blank=True, null=True, max_length=30)
    moneda = models.CharField(blank=True, null=True, max_length=20)
    pagado = models.BooleanField(blank=True, null=True, default=False)
    fecha_del_pago = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.user.name} - {self.cantidad} - {self.moneda}'