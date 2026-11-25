
from django.db import models

# Create your models here.
class Turma(models.Model):
    turma = models.CharField(max_length=100, unique=True)
    dia_semana = models.CharField(max_length=14)
    turno = models.CharField(max_length=20)

    def __str__(self):
        return self.turma


class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=255)
    turma = models.ForeignKey(
        Turma,
        on_delete=models.PROTECT,
        related_name='alunos'
    )
    matricula = models.CharField(max_length=20, unique=True)
    situacao = models.BooleanField(True)

    def __str__(self):
        return self.nome_aluno
