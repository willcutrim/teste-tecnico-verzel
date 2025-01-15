from django.db.models import Count
from .models import Alocacao
from programadores.models import Programador
from projetos.models import Projeto

class AlocacoesRules:
    model_object = Alocacao

    @property
    def alocacao(self):
        return self.model_object

    def _obter_programador(self, **kwargs):
        return Programador.objects.get(id=kwargs.get('programador'))
    
    def _obter_projeto(self, **kwargs):
        return Projeto.objects.get(id=kwargs.get('projeto'))

    def tecnologias(self, **kwargs) -> bool:
        programador = self._obter_programador(**kwargs)
        projeto = self._obter_projeto(**kwargs)

        query = Programador.objects.filter(
            id=programador.id,
            tecnologias__in=projeto.tecnologias.all()
        ).annotate(
            num_tecnologias=Count('tecnologias')
        ).filter(
            num_tecnologias__gt=0
        )

        programador_qualificado = query.exists()
        return programador_qualificado
    
    def rule_programador_em_projeto(self, **kwargs) -> tuple:
        programador_em_projeto = self.alocacao.objects.filter(
            projeto=kwargs.get('projeto'), 
            desenvolvedor=kwargs.get('programador')
        ).exists()
        if programador_em_projeto:
            return False, 'Programador já faz parte desse projeto.'
        
        return True, ''
    
    def rule_validar_tecnologias(self, **kwargs) -> tuple:
        if not self.tecnologias(**kwargs):
            return False, 'Programador não possui os requisitos necessários.'
        
        return True, ''
    
    def rule_validar_periodo(self, **kwargs) -> tuple:
        projeto = self._obter_projeto(**kwargs)
        if kwargs.get('horas') > (projeto.data_final - projeto.data_inicial).days * 24:
            return False, 'As horas planejadas estão fora do intervalo definido pelo projeto.'
        
        return True, ''
    
    def can_criar_alocacoes(self, **kwargs) -> tuple:
        """
            Função que chama todas as regras e retorna a primeira que não for satisfeita.
        """
        regras = [
            self.rule_programador_em_projeto,
            self.rule_validar_tecnologias,
            self.rule_validar_periodo
        ]

        for regra in regras:
            resultado, mensagem = regra(**kwargs)
            if not resultado:
                return resultado, mensagem
        
        return True, ''
