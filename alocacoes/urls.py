from django.urls import path

from . import views

urlpatterns = [
    path('listar_alocacoes/', views.AlocacoesAllListView.as_view(), name='listar-alocacoes'),
    path('filtrar/<int:projeto_id>/', views.AlocacoesPorProjetoView.as_view(), name='filtrar'),
    path('criar_alocacao/', views.AlocacoesCriarAlocaaoCreateView.as_view(), name='criar-alocacao'),
    path('deletar_alocacao/<int:alocacao_id>/', views.AlocacoesDeletarAlocaaoDeleteView.as_view(), name='deletar-alocacao'),
    path('atualizar_alocacao/<int:alocacao_id>/', views.AlocacoesAlterarAlocaaoUpdateView.as_view(), name='atualizar-alocacao'),
]
