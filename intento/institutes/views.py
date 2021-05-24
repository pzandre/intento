from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Institute, Discipline, DisciplineMacroContent, DisciplineMicroContent
from .forms import DisciplineForm, InstituteForm, DisciplineMacroForm, DisciplineMicroForm


class CreateDiscipline(CreateView):
    model = Discipline
    template_name = 'new_discipline.html'
    form_class = DisciplineForm


class CreateMacro(CreateView):
    model = DisciplineMacroContent
    template_name = 'new_macro.html'
    form_class = DisciplineMacroForm


class CreateMicro(CreateView):
    model = DisciplineMicroContent
    template_name = 'new_micro.html'
    form_class = DisciplineMicroForm


class UpdateInstitute(UpdateView):
    model = Institute
    template_name = 'update_institute.html'
    form_class = InstituteForm


class UpdateDiscipline(UpdateView):
    model = Discipline
    template_name = 'update_discipline.html'
    form_class = DisciplineForm


class UpdateMacro(UpdateView):
    model = DisciplineMacroContent
    template_name = 'update_macro.html'
    form_class = DisciplineMacroForm


class UpdateMicro(UpdateView):
    model = DisciplineMicroContent
    template_name = 'update_micro.html'
    form_class = DisciplineMicroForm


class DeleteDiscipline(DeleteView):
    model = Discipline
    template_name = 'delete_discipline.html'
    success_url = reverse_lazy('disciplines')


class DeleteMacro(DeleteView):
    model = DisciplineMacroContent
    template_name = 'delete_macro.html'
    success_url = reverse_lazy('disciplines')


class DeleteMicro(DeleteView):
    model = DisciplineMicroContent
    template_name = 'delete_micro.html'
    success_url = reverse_lazy('disciplines')


class InstituteDetail(DetailView):
    model = Institute
    template_name = 'institute_detail.html'


class DisciplineDetail(DetailView):
    model = Discipline
    template_name = 'discipline_detail.html'


class MacroDetail(DetailView):
    model = DisciplineMacroContent
    template_name = 'macro_detail.html'


class MicroDetail(DetailView):
    model = DisciplineMicroContent
    template_name = 'micro_detail.html'


class DisciplineList(ListView):
    model = Discipline
    template_name = 'disciplines.html'
    paginate_by = 10
    ordering = ['name']


class MacroList(ListView):
    model = DisciplineMacroContent
    template_name = 'macros.html'
    paginate_by = 10
    ordering = ['discipline', 'macro_content']


class MicroList(ListView):
    model = DisciplineMicroContent
    template_name = 'micros.html'
    paginate_by = 10
    ordering = ['macro_content', 'micro_content']

