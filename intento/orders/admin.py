from django.contrib import admin
from .models import QuestionOrder, Question

admin.site.register(QuestionOrder)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
