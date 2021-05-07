from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
        widgets = {
            'question': forms.HiddenInput()
        }


class UpdateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class UpdateAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
        widgets = {
            'question': forms.HiddenInput()
        }
