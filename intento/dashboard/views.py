from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AnswerForm, QuestionForm, UpdateAnswerForm, UpdateQuestionForm
from .models import Answer, Question


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

    def get_initial(self):
        initial = super().get_initial()
        initial['question'] = Question.objects.get(pk=self.kwargs['pk'])
        return initial

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = Question.objects.get(id=self.kwargs['pk'])
        return context


class QuestionDetailView(DetailView):
    model = Answer
    template_name = 'question_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = Question.objects.get(id=self.kwargs['pk'])
        return context


class UpdateQuestionView(UpdateView):
    model = Question
    form_class = UpdateQuestionForm
    template_name = 'update_question.html'

    def get_success_url(self):
        view_name = 'question-detail'
        return reverse(view_name, kwargs={'pk': self.object.pk})


class UpdateAnswerView(UpdateView):
    model = Answer
    form_class = UpdateAnswerForm
    template_name = 'update_answer.html'

    def get_success_url(self):
        view_name = 'question-detail'
        return reverse(view_name, kwargs={'pk': self.object.pk})


class QuestionListView(ListView):
    model = Question
    template_name = 'questions.html'


class QuestionSearchView(ListView):
    models = Question
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Question.objects.filter(Q(base_text__icontains=query)) | \
                          Question.objects.filter(Q(bibliographic_reference__icontains=query)) | \
                          Question.objects.filter(Q(question_statement__icontains=query)) | \
                          Question.objects.filter(Q(answer_A__icontains=query)) | \
                          Question.objects.filter(Q(answer_B__icontains=query)) | \
                          Question.objects.filter(Q(answer_C__icontains=query)) | \
                          Question.objects.filter(Q(answer_D__icontains=query)) | \
                          Question.objects.filter(Q(answer_E__icontains=query))
        else:
            object_list = None
        return object_list


class DeleteQuestionView(DeleteView):
    model = Question
    template_name = 'delete_question.html'
    success_url = reverse_lazy('question-list')
