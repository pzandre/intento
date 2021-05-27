from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Institute, Discipline, DisciplineMacroContent, DisciplineMicroContent
from .forms import DisciplineForm, InstituteForm, DisciplineMacroForm, DisciplineMicroForm


class CreateDiscipline(LoginRequiredMixin, CreateView):
    model = Discipline
    template_name = 'new_discipline.html'
    form_class = DisciplineForm


class CreateMacro(LoginRequiredMixin, CreateView):
    model = DisciplineMacroContent
    template_name = 'new_macro.html'
    form_class = DisciplineMacroForm


class CreateMicro(LoginRequiredMixin, CreateView):
    model = DisciplineMicroContent
    template_name = 'new_micro.html'
    form_class = DisciplineMicroForm


class UpdateInstitute(LoginRequiredMixin, UpdateView):
    model = Institute
    template_name = 'update_institute.html'
    form_class = InstituteForm


class UpdateDiscipline(LoginRequiredMixin, UpdateView):
    model = Discipline
    template_name = 'update_discipline.html'
    form_class = DisciplineForm


class UpdateMacro(LoginRequiredMixin, UpdateView):
    model = DisciplineMacroContent
    template_name = 'update_macro.html'
    form_class = DisciplineMacroForm


class UpdateMicro(LoginRequiredMixin, UpdateView):
    model = DisciplineMicroContent
    template_name = 'update_micro.html'
    form_class = DisciplineMicroForm


class DeleteDiscipline(LoginRequiredMixin, DeleteView):
    model = Discipline
    template_name = 'delete_discipline.html'
    success_url = reverse_lazy('disciplines')


class DeleteMacro(LoginRequiredMixin, DeleteView):
    model = DisciplineMacroContent
    template_name = 'delete_macro.html'
    success_url = reverse_lazy('disciplines')


class DeleteMicro(LoginRequiredMixin, DeleteView):
    model = DisciplineMicroContent
    template_name = 'delete_micro.html'
    success_url = reverse_lazy('disciplines')


class InstituteDetail(LoginRequiredMixin, DetailView):
    model = Institute
    template_name = 'institute_detail.html'


class DisciplineDetail(LoginRequiredMixin, DetailView):
    model = Discipline
    template_name = 'discipline_detail.html'


class MacroDetail(LoginRequiredMixin, DetailView):
    model = DisciplineMacroContent
    template_name = 'macro_detail.html'


class MicroDetail(LoginRequiredMixin, DetailView):
    model = DisciplineMicroContent
    template_name = 'micro_detail.html'


class DisciplineList(LoginRequiredMixin, ListView):
    model = Discipline
    template_name = 'disciplines.html'
    paginate_by = 10
    ordering = ['name']


class MacroList(LoginRequiredMixin, ListView):
    model = DisciplineMacroContent
    template_name = 'macros.html'
    paginate_by = 10
    ordering = ['discipline', 'macro_content']


class MicroList(LoginRequiredMixin, ListView):
    model = DisciplineMicroContent
    template_name = 'micros.html'
    paginate_by = 10
    ordering = ['macro_content', 'micro_content']

