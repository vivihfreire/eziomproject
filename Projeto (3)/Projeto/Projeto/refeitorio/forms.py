
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

        widgets = {
            "nome_aluno": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o nome"
                }
            ),

            "turma": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "matricula": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite a matrícula"
                }
            ),

            "situacao": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite a situação"
                }
            ),
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

        widgets = {
            "turma": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o nome da turma"
                }
            ),

            "dia_semana": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o dia da semana"
                }
            ),
            
            "turno": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o turno"
                }
            ),
        }
