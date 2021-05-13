from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from members.models import Institute, Profile


class Discipline(models.Model):
    course = models.CharField(max_length=255)
    macro_content = models.CharField(max_length=255)
    micro_content = models.CharField(max_length=255)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('home')



class QuestionOrder(models.Model):
    institute = models.ForeignKey(Institute, verbose_name="Institute", on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, verbose_name="Discipline", on_delete=models.CASCADE)
    teacher = models.ForeignKey(Profile, verbose_name="Teacher", on_delete=models.CASCADE)
    question_quantity = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    order_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now=False)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('home')
