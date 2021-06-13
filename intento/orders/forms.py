from django import forms
from taggit.forms import TagWidget
from bootstrap_datepicker_plus import DatePickerInput
from .models import QuestionOrder, Question
from institutes.models import Discipline, DisciplineMacroContent, DisciplineMicroContent
from users.models import CustomUser
from django.urls import reverse_lazy


class QuestionOrderForm(forms.ModelForm):

    class Meta:
        model = QuestionOrder
        fields = '__all__'

        widgets = {
            'due_date': DatePickerInput(),  # "(format='%d-%m-%Y').start_of('order_date'),
            'institute': forms.Select(attrs={'id': 'institute', 'class': 'form-control'}),
            'discipline': forms.Select(attrs={'id': 'discipline', 'class': 'form-control',
                                              'discipline-queries-url': reverse_lazy('ajax-load-discipline')}),
            'macro_content': forms.Select(attrs={'id': 'macro_content', 'class': 'form-control',
                                                 'macro-queries-url': reverse_lazy('ajax-load-macro')}),
            'micro_content': forms.Select(attrs={'id': 'micro_content', 'class': 'form-control',
                                                 'micro-queries-url': reverse_lazy('ajax-load-micro')}),
            'question_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'id': 'teacher', 'class': 'form-control',
                                           'teacher-queries-url': reverse_lazy('ajax-load-teacher')}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['discipline'].queryset = Discipline.objects.none()
        self.fields['macro_content'].queryset = DisciplineMacroContent.objects.none()
        self.fields['micro_content'].queryset = DisciplineMacroContent.objects.none()
        self.fields['teacher'].queryset = CustomUser.objects.none()

        if 'institute' in self.data:
            try:
                institute_id = int(self.data.get('institute'))
                self.fields['discipline'].queryset = Discipline.objects.filter(institute=institute_id).order_by('name')
                self.fields['teacher'].queryset = CustomUser.objects.filter(institute=institute_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['discipline'].queryset = self.instance.institute.discipline_set.order_by('name')
            self.fields['teacher'].queryset = self.instance.institute.teacher_set.order_by('name')
        if 'discipline' in self.data:
            try:
                discipline_id = int(self.data.get('discipline'))
                self.fields['macro_content'].queryset = DisciplineMacroContent.objects.filter(
                    discipline=discipline_id).order_by('macro_content')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['macro_content'].queryset = self.instance.discipline.disciplinemacrocontent_set.order_by(
                'macro_content')
        if 'macro_content' in self.data:
            try:
                macro_content_id = int(self.data.get('macro_content'))
                self.fields['micro_content'].queryset = DisciplineMicroContent.objects.filter(
                    macro_content=macro_content_id).order_by('micro_content')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields[
                'micro_content'].queryset = self.instance.disciplinemacrocontent.disciplinemicrocontent_set.order_by(
                'micro_content')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'question_type': forms.Select(attrs={'class': 'form-control'}),
            'bibliographic_reference_1': forms.TextInput(attrs={'class': 'form-control'}),
            'bibliographic_reference_2': forms.TextInput(attrs={'class': 'form-control'}),
            'bibliographic_reference_3': forms.TextInput(attrs={'class': 'form-control'}),
            'question_order': forms.HiddenInput(),
            'id_by_order': forms.HiddenInput(),
            'difficulty': forms.Select(attrs={'class': 'form-control', 'style': 'display:none'}),
            'bloom_taxonomy': forms.Select(attrs={'class': 'form-control', 'style': 'display:none'}),
            'question_information': forms.Select(attrs={'class': 'form-control', 'style': 'display:none'}),
            'correct_answer': forms.Select(attrs={'class': 'form-control', 'style': 'display:none'}),
            'a_justification': forms.TextInput(attrs={'style': 'display:none'}),
            'b_justification': forms.TextInput(attrs={'style': 'display:none'}),
            'c_justification': forms.TextInput(attrs={'style': 'display:none'}),
            'd_justification': forms.TextInput(attrs={'style': 'display:none'}),
            'e_justification': forms.TextInput(attrs={'style': 'display:none'}),
            'revision_approval': forms.CheckboxInput(attrs={'style': 'display:none'}),
            'tag': TagWidget(attrs={'data-role': 'tagsinput', 'class': 'form-control', 'style': 'display:none'}),
        }
