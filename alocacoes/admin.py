from django.contrib import admin
from .models import Alocacao

@admin.register(Alocacao)
class AlocacaoAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'desenvolvedor', 'horas')
    search_fields = ('projeto__nome', 'desenvolvedor__nome')
