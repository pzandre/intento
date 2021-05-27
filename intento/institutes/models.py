from django.db import models
from django.urls import reverse


class Institute(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Discipline(models.Model):
    institute = models.ForeignKey(Institute, verbose_name='institute', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)

    @staticmethod
    def get_absolute_url():
        return reverse('home')

    def __str__(self):
        return str(self.name)


class DisciplineMacroContent(models.Model):
    discipline = models.ForeignKey(Discipline, verbose_name='discipline', on_delete=models.CASCADE)
    macro_content = models.CharField(max_length=255)

    def __str__(self):
        return str(self.macro_content)


class DisciplineMicroContent(models.Model):
    macro_content = models.ForeignKey(DisciplineMacroContent, verbose_name='macro_content', on_delete=models.CASCADE)
    micro_content = models.CharField(max_length=255)

    def __str__(self):
        return str(self.micro_content)
