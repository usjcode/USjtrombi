from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class EmailUser(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    