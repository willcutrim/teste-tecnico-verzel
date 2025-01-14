from django.urls import path

from . import views

urlpatterns = [
    path('listar_programadores/', views.ProgramadoresListarTodosProgramadoresListView.as_view(), name='listar-programadores'),
    path('criar_programador/', views.ProgramadoresCriarProgramadorView.as_view(), name='criar-programador'),
    path(
        'deletar_programador/<int:programador_id>/', 
        views.ProgramadoresDeletarProgramadorDeleteView.as_view(), 
        name='deletar-programador'
    ),
    path('filtrar/<int:programador_id>/', views.ProgramadoresFiltrarPorIDView.as_view(), name='filtrar'),

]
