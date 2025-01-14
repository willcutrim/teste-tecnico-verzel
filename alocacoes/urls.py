from django.urls import path

from . import views

urlpatterns = [
    path('all_alocacoes/', views.AlocacoesAllListView.as_view(), name='all-alocacoes'),
]
