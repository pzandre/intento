from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AnswerForm, QuestionForm, UpdateAnswerForm, UpdateQuestionForm
from .models import Answer, Question
from courses.models import QuestionOrder
from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import CONTENT_TYPE_PNG, WeasyTemplateResponse


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'dashboard.html')


class CreateQuestionView(CreateView):
    model = Question
    template_name = 'new_question.html'
    form_class = QuestionForm

    def get_initial(self):
        initial = super().get_initial()
        initial['question_order'] = QuestionOrder.objects.get(pk=self.kwargs['question_order'])
        initial['id_by_order'] = self.kwargs['id_by_order']
        return initial

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question_order'] = QuestionOrder.objects.get(id=self.kwargs.get('question_order')).id
        context['id_by_order'] = self.kwargs['id_by_order']
        return context

    def get_success_url(self):
        view_name = 'new-answer'
        return reverse(view_name, kwargs={'question_order': self.object.question_order.id,
                                          'id_by_order': self.object.id_by_order})


class CreateAnswerView(CreateView):
    model = Answer
    template_name = 'new_answer.html'
    form_class = AnswerForm

    def get_initial(self):
        order_tag = QuestionOrder.objects.get(pk=self.kwargs['question_order'])
        initial = super().get_initial()
        initial['question'] = Question.objects.filter(
            question_order=order_tag).get(id_by_order=self.kwargs['id_by_order'])
        initial['tag'] = order_tag.discipline.course
        return initial

    def get_success_url(self):
        view_name = 'question-detail'
        return reverse(view_name, kwargs={'question_order': self.kwargs['question_order'],
                                          'id_by_order': self.kwargs['id_by_order']})


class QuestionDetailView(DetailView):
    model = Answer
    template_name = 'question_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = Question.objects.filter(
            question_order=self.kwargs['question_order']).get(id_by_order=self.kwargs['id_by_order'])
        context['question_order'] = self.kwargs['question_order']
        context['id_by_order'] = self.kwargs['id_by_order']
        return context

    def get_object(self):
        return get_object_or_404(Answer, pk=self.kwargs['question_order'])


class UpdateQuestionView(UpdateView):
    model = Question
    form_class = UpdateQuestionForm
    template_name = 'update_question.html'

    def get_success_url(self):
        view_name = 'question-detail'
        return reverse(view_name, kwargs={'question_order': self.object.question_order.id,
                                          'id_by_order': self.object.id_by_order})


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


class QuestionsPDFListView(ListView):
    template_name = 'question_list_pdf_view.html'

    def get_queryset(self, *args, **kwargs):
        self.order_pk = get_object_or_404(QuestionOrder, pk=self.kwargs['question_order'])
        return Question.objects.filter(question_order=self.order_pk)


class CustomWeasyTemplateResponse(WeasyTemplateResponse):
    # customized response class to change the default URL fetcher
    def get_url_fetcher(self):
        # disable host and certificate check
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return functools.partial(django_url_fetcher, ssl_context=context)


class PatientAppointmentsPrintView(WeasyTemplateResponseMixin, QuestionsPDFListView):
    # output of MyModelView rendered as PDF with hardcoded CSS
    pdf_stylesheets = [
        'static/css/bootstrap.min.css',
        'static/css/katex.min.css',
        'monokai-sublime.min.css',
    ]
    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = True
    # custom response class to configure url-fetcher
    response_class = CustomWeasyTemplateResponse


class QuestionListDownloadView(WeasyTemplateResponseMixin, QuestionsPDFListView):
    # suggested filename (is required for attachment/download!)
    pdf_filename = 'simulado.pdf'
