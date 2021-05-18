from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Discipline, QuestionOrder


class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = '__all__'


class QuestionOrderForm(forms.ModelForm):
    class Meta:
        model = QuestionOrder
        fields = '__all__'

        widgets = {
            'due_date': DatePickerInput(),
        }


class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = QuestionOrder
        fields = '__all__'


class UpdateDisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = '__all__'
