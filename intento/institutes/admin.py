from django.contrib import admin
from .models import Institute, Discipline, DisciplineMacroContent, DisciplineMicroContent

admin.site.register(Institute)
admin.site.register(Discipline)
admin.site.register(DisciplineMacroContent)
admin.site.register(DisciplineMicroContent)
