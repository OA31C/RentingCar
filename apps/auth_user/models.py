from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from renting_car.settings import LANGUAGE_CODE


# Create your models here.
class User(AbstractUser):
    LANGUAGES = (
        ('en', 'English'),
        ('ru', 'Russia')
    )

    email = models.EmailField(
        verbose_name=_('E-mail'),
        max_length=60,
        unique=True)

    language = models.CharField(
        max_length=5,
        verbose_name=_('Language'),
        choices=LANGUAGES,
        default=LANGUAGE_CODE)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"id:{self.id}, {self.username}"
