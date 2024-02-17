from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    first_name = models.CharField(null=True, blank=True, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.email
    