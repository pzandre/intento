from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from members.models import Institute, Profile
from dashboard.models import Answer, Question

class Discipline(models.Model):
    course = models.CharField(max_length=255)
    macro_content = models.CharField(max_length=255)
    micro_content = models.CharField(max_length=255)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('home')

    def __str__(self):
        return str(self.course)


class QuestionOrder(models.Model):
    institute = models.ForeignKey(Institute, verbose_name="Institute", on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, verbose_name="Discipline", on_delete=models.CASCADE)
    teacher = models.ForeignKey(Profile, verbose_name="Teacher", on_delete=models.CASCADE)
    question_quantity = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    order_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now=False)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('order-detail')

    @property
    def question_range(self):
        return range(self.question_quantity)

    @property
    def question_details(self, *args, **kwargs):
        order = Question.objects.get(question_order=self.pk)
        return order


