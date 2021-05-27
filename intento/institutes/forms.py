from django import forms
from .models import Discipline, Institute, DisciplineMacroContent, DisciplineMicroContent


class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = '__all__'


class InstituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = '__all__'


class DisciplineMacroForm(forms.ModelForm):
    class Meta:
        model = DisciplineMacroContent
        fields = '__all__'


class DisciplineMicroForm(forms.ModelForm):
    class Meta:
        model = DisciplineMicroContent
        fields = '__all__'
