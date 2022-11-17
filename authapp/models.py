from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(blank=True, verbose_name='Email', unique=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Возраст')
    avatar = models.ImageField(upload_to='users', blank=True, null=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
