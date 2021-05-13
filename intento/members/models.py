from django.db import models
from django.contrib.auth.models import User


class Institute(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute, verbose_name='institute', on_delete=models.CASCADE)

    ADMIN = 'AD'
    VALIDATOR = 'VD'
    TEACHER = 'TC'

    PERMISSION_CHOICES = [(ADMIN, 'Administrador(a)'), (VALIDATOR, 'Validador(a) de Questões'),
                          (TEACHER, 'Professor(a)')]

    permissions = models.CharField(max_length=2, choices=PERMISSION_CHOICES)

    def __str__(self):
        return str(self.user)
