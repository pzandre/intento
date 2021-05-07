from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'dashboard.html')


class CreateQuestionView(CreateView):
    model = Question
    template_name = 'new_question.html'
    form_class = QuestionForm


class CreateAnswerView(CreateView):
    model = Answer
    template_name = 'new_answer.html'
    form_class = AnswerForm
    # success_url = reverse_lazy('question-detail')

    def get_initial(self):
        initial = super().get_initial()
        initial['question'] = Question.objects.get(pk=self.kwargs['pk'])
        return initial

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = Question.objects.get(id=self.kwargs['pk'])
        return context


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question_details.html'
