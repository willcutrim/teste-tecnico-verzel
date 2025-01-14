from django.contrib import admin
from .models import Programador


admin.site.register(Programador)
class ProgramadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tecnologias')
    search_fields = ('nome', 'tecnologias__nome')
