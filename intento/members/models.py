from django.db import models
from django.contrib.auth.models import User


class Institute(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
