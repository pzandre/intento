from django.contrib import admin
# Register your models here.
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Question)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Answer)
