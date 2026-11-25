from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from .models import Aluno, Turma
from .forms import AlunoForm, TurmaForm


class IndexTemplateView(TemplateView):
    # Retorna uma resposta HTTP com o conteúdo "Página Inicial"
    template_name = 'refeitorio/index.html'


# Views de Aluno

class AlunoListView(ListView):
    model = Aluno
    template_name = 'refeitorio/aluno_list.html'
    context_object_name = 'alunos'


class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'refeitorio/aluno_create.html'
    success_url = reverse_lazy('aluno_list')


class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'refeitorio/aluno_create.html'
    success_url = reverse_lazy('aluno_list')


class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'refeitorio/aluno_confirm_delete.html'
    success_url = reverse_lazy('aluno_list')

class AlunoDetailView(DetailView):
    model = Aluno
    template_name = 'refeitorio/aluno_detail.html'


# Views de Turma

class TurmaListView(ListView):
    model = Turma
    template_name = 'refeitorio/turma_list.html'
    context_object_name = 'turmas'


class TurmaCreateView(CreateView):
    model = Turma
    form_class = TurmaForm
    template_name = 'refeitorio/turma_create.html'
    success_url = reverse_lazy('turma_list')


class TurmaUpdateView(UpdateView):
    model = Turma
    form_class = TurmaForm
    template_name = 'refeitorio/turma_create.html'
    success_url = reverse_lazy('turma_list')



class TurmaDeleteView(DeleteView):
    model = Turma
    template_name = 'refeitorio/turma_confirm_delete.html'
    success_url = reverse_lazy('turma_list')

class TurmaDetailView(DetailView):
    model = Turma
    template_name = 'refeitorio/turma_detail.html'
