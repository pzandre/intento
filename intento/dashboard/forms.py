from django import forms
from tinymce.widgets import TinyMCE
from .models import Question, Answers

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        