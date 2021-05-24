from django.contrib import admin
from .models import QuestionOrder, Question, Answer

admin.site.register(QuestionOrder)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
