from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer


def home(request):
    return HttpResponse("<h1>This is the home page</h1>")


class CreateQuestionView(CreateView):
    model = Question
    template_name = 'new_question.html'
    form_class = QuestionForm
    success_url = reverse_lazy('new-answer')


class CreateAnswerView(CreateView):
    model = Answer
    # template_name = 'new_answer.html'
    form_class = AnswerForm
    success_url = reverse_lazy('home')

    def get(self, request):
        question = Question.objects.get(id=1)
        context = {'question': question.__dict__}
        # form = self.form_class
        return render(request, 'new_answer.html', context)
