from django.urls import path

from . import views

urlpatterns = [
    path('criar_projeto/', views.ProjetosCriarProjetoCreateView.as_view(), name='criar-projeto'),
    path('deletar_projeto/<int:projeto_id>/', views.ProjetosDeletarProjetoDeleteView.as_view(), name='deletar-projeto'),
    path(
        'atualizar_projeto/<int:projeto_id>/', views.ProjetosAtualizarProjetoUpdateView.as_view(), name='atualizar-projeto'
    ),
    path('filtrar/<int:projeto_id>/', views.ProjetosFiltrarPorIDView.as_view(), name='filtrar'),
    
]
