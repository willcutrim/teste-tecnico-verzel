from django.urls import path
from . import views

urlpatterns = [
    path('listar_tecnologias/', views.TecnologiasListarTecnologiasListView.as_view(), name='listar-tecnologias'),
    path('criar_tecnologia/', views.TecnologiasCriarTecnologiaCreateView.as_view(), name='criar-tecnologia'),
    path(
        'deletar_tecnologia/<int:tecnologia_id>/', 
        views.TecnologiasDeletarTecnologiaDeleteView.as_view(), 
        name='deletar-tecnologia'
    ),
]
