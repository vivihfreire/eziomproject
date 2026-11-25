from . import views 
from django.urls import path



urlpatterns = [
    path('index/', views.IndexTemplateView.as_view(), name='index'),
    
    path('alunos/', views.AlunoListView.as_view(), name='aluno_list'),
    path('turmas/', views.TurmaListView.as_view(), name='turma_list'),

    path('aluno/cadastrar/', views.AlunoCreateView.as_view(), name='aluno_create'),
    path('aluno/atualizar/<int:pk>/', views.AlunoUpdateView.as_view(), name='aluno_update'),
    path('aluno/deletar/<int:pk>/', views.AlunoDeleteView.as_view(), name='aluno_delete'),
    path('aluno/detalhar/<int:pk>/', views.AlunoDetailView.as_view(), name='aluno_detail'),
    
    
    path('turma/cadastrar/', views.TurmaCreateView.as_view(), name='turma_create'),
    path('turma/atualizar/<int:pk>/', views.TurmaUpdateView.as_view(), name= 'turma_update'),
    path('turma/deletar/<int:pk>/', views.TurmaDeleteView.as_view(), name='turma_delete'),
    path('turma/detalhar/<int:pk>/', views.TurmaDetailView.as_view(), name='turma_detail'),
]