from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    languages = (
        (1, 'en'),
        (2, 'ru')
    )
    email = models.EmailField(max_length=60, unique=True)
    language = models.IntegerField(
        verbose_name='language', choices=languages, default='1')

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"id:{self.id}, {self.username}"
