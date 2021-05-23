from django import forms
from .models import Question, Answer


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


class UpdateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

        widgets = {
            'question_order': forms.HiddenInput(),
            'id_by_order': forms.HiddenInput()
        }


class UpdateAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
        widgets = {
            'question': forms.HiddenInput()
        }

