from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class User(AbstractUser):
    LANGUAGES = (
        (1, 'en'),
        (2, 'ru')
    )

    email = models.EmailField(
        verbose_name=_('E-mail'),
        max_length=60,
        unique=True)

    language = models.IntegerField(
        verbose_name=_('Language'),
        choices=LANGUAGES,
        default='en')

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"id:{self.id}, {self.username}"
