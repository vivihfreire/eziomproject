from django import forms
from .models import Aluno
from .models import Turma

class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'
        labels = {
            "nome_aluno": "Nome",
            "turma": "Turma",
            "matricula": "Matricula",
            "situacao": "Situação"
        }

class TurmaForm(forms.ModelForm):

    class Meta:
        model = Turma
        fields = '__all__'
        labels = {
            "turma": "Nome",
            "dia_semana": "Dia da Semana",
            "turno": "Turno"
        }