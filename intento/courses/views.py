from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Discipline, QuestionOrder
from .forms import DisciplineForm, QuestionOrderForm, UpdateDisciplineForm, UpdateOrderForm


class DisciplineListView(ListView):
    model = Discipline
    template_name = 'discipline_list.html'


class QuestionOrderListView(ListView):
    model = QuestionOrder
    template_name = 'orders.html'


class DisciplineDetailView(DetailView):
    model = Discipline
    template_name = 'discipline_details.html'


class QuestionOrderDetailView(DetailView):
    model = QuestionOrder
    template_name = 'order_details.html'


class CreateDisciplineView(CreateView):
    model = Discipline
    template_name = 'new_discipline.html'
    form_class = DisciplineForm


class CreateQuestionOrderView(CreateView):
    model = QuestionOrder
    template_name = 'new_question_order.html'
    form_class = QuestionOrderForm


class DisciplineUpdateView(UpdateView):
    model = Discipline
    form_class = UpdateDisciplineForm
    template_name = 'update_discipline.html'

    def get_success_url(self):
        view_name = 'discipline-detail'
        return reverse(view_name, kwargs={'pk': self.object.pk})


class QuestionOrderUpdateView(UpdateView):
    model = QuestionOrder
    form_class = UpdateOrderForm
    template_name = 'update_order.html'

    def get_success_url(self):
        view_name = 'order-detail'
        return reverse(view_name, kwargs={'pk': self.object.pk})


class DeleteDisciplineView(DeleteView):
    model = Discipline
    template_name = 'delete_discipline.html'
    success_url = reverse_lazy('disciplines')


class DeleteOrderView(DeleteView):
    model = QuestionOrder
    template_name = 'delete_order.html'
    success_url = reverse_lazy('orders')
