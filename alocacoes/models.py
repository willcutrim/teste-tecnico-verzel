from django.db import models
from projetos.models import Projeto
from programadores.models import Programador


class Alocacao(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, null=True, blank=True, related_name='alocacoes')
    desenvolvedor = models.ForeignKey(
        Programador, on_delete=models.CASCADE, null=True, blank=True, related_name='alocacoes'
    )
    horas = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.desenvolvedor.nome} alocado no projeto {self.projeto.nome} por {self.horas} horas"
