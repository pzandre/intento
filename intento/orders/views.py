from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import QuestionOrder, Question, Answer
from institutes.models import Institute, Discipline, DisciplineMacroContent, DisciplineMicroContent
from .forms import QuestionOrderForm, AnswerForm, QuestionForm
from django_weasyprint import WeasyTemplateResponseMixin
from users.models import CustomUser
from django_weasyprint.views import CONTENT_TYPE_PNG, WeasyTemplateResponse


def load_discipline_details(request):
    institute_id = request.GET.get('institute_id')
    disciplines = Discipline.objects.filter(institute=institute_id).all()
    return render(request, 'load_discipline_dropdown_list.html', {'disciplines': disciplines})

def load_macro_details(request):
    discipline_id = request.GET.get('discipline_id')
    macro_contents = DisciplineMacroContent.objects.filter(discipline=discipline_id).all()
    return render(request, 'load_macro_dropdown_list.html', {'macro_contents': macro_contents})

def load_micro_details(request):
    macro_content_id = request.GET.get('macro_content_id')
    micro_contents = DisciplineMicroContent.objects.filter(macro_content=macro_content_id).all()
    return render(request, 'load_micro_dropdown_list.html', {'micro_contents': micro_contents})

def load_teacher_details(request):
    institute_id = request.GET.get('institute_id')
    teachers = CustomUser.objects.filter(institute=institute_id).all()
    return render(request, 'load_teacher_dropdown_list.html', {'teachers': teachers})


class OrderList(ListView):
    model = QuestionOrder
    template_name = 'orders.html'


class OrderDetail(DetailView):
    model = QuestionOrder
    template_name = 'order_details.html'


class CreateOrder(CreateView):
    model = QuestionOrder
    template_name = 'new_question_order.html'
    form_class = QuestionOrderForm


class UpdateOrder(UpdateView):
    model = QuestionOrder
    form_class = QuestionOrderForm
    template_name = 'update_order.html'

    def get_success_url(self):
        view_name = 'order-detail'
        return reverse(view_name, kwargs={'pk': self.object.pk})


class DeleteOrder(DeleteView):
    model = QuestionOrder
    template_name = 'delete_order.html'
    success_url = reverse_lazy('orders')


class CreateQuestion(CreateView):
    model = Question
    template_name = 'new_question.html'
    form_class = QuestionForm

    def get_initial(self):
        initial = super().get_initial()
        initial['question_order'] = QuestionOrder.objects.get(pk=self.kwargs['order'])
        initial['id_by_order'] = self.kwargs['id_by_order']
        return initial

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = QuestionOrder.objects.get(id=self.kwargs.get('order')).id
        context['id_by_order'] = self.kwargs['id_by_order']
        return context

    def get_success_url(self):
        view_name = 'create-answer'
        return reverse(view_name, kwargs={'order': self.object.order.id,
                                          'id_by_order': self.object.id_by_order})


class CreateAnswer(CreateView):
    model = Answer
    template_name = 'new_answer.html'
    form_class = AnswerForm

    def get_initial(self):
        order_tag = QuestionOrder.objects.get(pk=self.kwargs['order'])
        initial = super().get_initial()
        initial['question'] = Question.objects.filter(
            question_order=order_tag).get(id_by_order=self.kwargs['id_by_order'])
        initial['tag'] = order_tag.discipline.name
        return initial

    def get_success_url(self):
        view_name = 'question-detail'
        return reverse(view_name, kwargs={'order': self.kwargs['order'],
                                          'id_by_order': self.kwargs['id_by_order']})


class QuestionDetail(DetailView):
    model = Answer
    template_name = 'question_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = Question.objects.filter(
            question_order=self.kwargs['order']).get(id_by_order=self.kwargs['id_by_order'])
        context['order'] = self.kwargs['order']
        context['id_by_order'] = self.kwargs['id_by_order']
        return context

    def get_object(self):
        return get_object_or_404(Answer, pk=self.kwargs['order'])


class UpdateQuestion(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'update_question.html'

    def get_success_url(self):
        view_name = 'question-detail'
        return reverse(view_name, kwargs={'order': self.object.question_order.id,
                                          'id_by_order': self.object.id_by_order})


class UpdateAnswer(UpdateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'update_answer.html'

    def get_success_url(self):
        view_name = 'question-detail'
        return reverse(view_name, kwargs={
            'order': self.object.question.question_order.id,
            'id_by_order': self.object.pk})


class QuestionList(ListView):
    model = Question
    template_name = 'questions.html'


class QuestionSearch(ListView):
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


class DeleteQuestion(DeleteView):
    model = Question
    template_name = 'delete_question.html'
    success_url = reverse_lazy('question-list')


class QuestionsPDFList(ListView):
    template_name = 'question_list_pdf_view.html'

    def get_queryset(self, *args, **kwargs):
        self.order_pk = get_object_or_404(QuestionOrder, pk=self.kwargs['order'])
        return Question.objects.filter(question_order=self.order_pk)


class CustomWeasyTemplateResponse(WeasyTemplateResponse):
    # customized response class to change the default URL fetcher
    def get_url_fetcher(self):
        # disable host and certificate check
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return functools.partial(django_url_fetcher, ssl_context=context)


class QuestionListPrint(WeasyTemplateResponseMixin, QuestionsPDFList):
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


class QuestionListDownload(WeasyTemplateResponseMixin, QuestionsPDFList):
    # suggested filename (is required for attachment/download!)
    pdf_filename = 'simulado.pdf'
