from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import QuestionOrder, Question, Answer
from institutes.models import Institute, Discipline, DisciplineMacroContent, DisciplineMicroContent
from users.models import CustomUser

class QuestionOrderForm(forms.ModelForm):
    # institute = forms.CharField(max_length=255, label="Institute",
    #                                widget=forms.Select(
    #                                attrs={'class': 'form-control'}))

    class Meta:
        model = QuestionOrder
        fields = '__all__'

        widgets = {
            'due_date': DatePickerInput(),
            'institute': forms.Select(attrs={'id': 'institute', 'class': 'form-control'}),
            'discipline': forms.Select(attrs={'id': 'discipline', 'class': 'form-control',
                                              'discipline-queries-url': '{% url "ajax-load-discipline" %}'}),
            'macro_content': forms.Select(attrs={'id': 'macro-content', 'class': 'form-control',
                                                 'data-queries-url': "{% url 'ajax-load-macro' %}"}),
            'micro_content': forms.Select(attrs={'id': 'micro-content', 'class': 'form-control',
                                                 'data-queries-url': "{% url 'ajax-load-micro' %}"}),
            'teacher': forms.Select(attrs={'id': 'teacher', 'class': 'form-control',
                                           'data-queries-url': "{% url 'ajax-load-teacher' %}"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['discipline'].queryset = Discipline.objects.none()
        self.fields['macro_content'].queryset = DisciplineMacroContent.objects.none()
        self.fields['micro_content'].queryset = DisciplineMicroContent.objects.none()
        self.fields['teacher'].queryset = CustomUser.objects.none()

        if 'institute' in self.data:
            try:
                institute_id = int(self.data.get('institute'))
                self.fields['discipline'].queryset = Discipline.objects.filter(institute=institute_id).order_by('name')
                discipline_id = int(self.data.get('discipline'))
                self.fields['macro_content'].queryset = DisciplineMacroContent.objects.filter(
                    discipline=discipline_id).order_by('macro_content')
                macro_content_id = int(self.data.get('macro_content'))
                self.fields['micro_content'].queryset = DisciplineMicroContent.objects.filter(
                    macro_content=macro_content_id).order_by('micro_content')
                self.fields['teacher'].queryset = CustomUser.objects.filter(institute=institute_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['discipline'].queryset = self.instance.institute.discipline_set.order_by('name')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'question_order': forms.HiddenInput(),
            'id_by_order': forms.HiddenInput()
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
        widgets = {
            'question': forms.HiddenInput(),
            'revision_approval': forms.HiddenInput(),
        }


