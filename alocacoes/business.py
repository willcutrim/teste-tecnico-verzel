from alocacoes.models import Alocacao
from programadores.models import Programador
from projetos.models import Projeto
from .rules import AlocacoesRules


class AlocacoesBusiness:
    model_object = Alocacao
    rules = AlocacoesRules()

    @property
    def alocacoes(self):
        return self.model_object
    
    def _get_alocacao(self, **kwargs):
            try:
                alocacao = self.model_object.objects.get(id=kwargs.get('alocacao_id'))
                return alocacao
            
            except self.alocacoes.DoesNotExist:
                return None

    def criar_alocacao(self, **kwargs):
        try:
            projeto = Projeto.objects.get(id=kwargs.get('projeto'))
            desenvolvedor = Programador.objects.get(id=kwargs.get('programador'))

            rules = self.rules.can_criar_alocacoes(**kwargs)

            if rules:
                return [], rules

            alocacao = self.alocacoes(
                projeto=projeto,
                desenvolvedor=desenvolvedor,
                horas=kwargs.get('horas')
            )
            alocacao.save()

            return alocacao, []
        
        except Exception as err:
            raise Exception('Erro ao criar alocação')
    
    def deletar_alocacao(self, **kwargs):
        try:
            alocacao = self._get_alocacao(**kwargs)
            if not alocacao:
                return None
            
            alocacao.delete()

        except Exception as err:
            raise Exception('Erro ao deletar alocação')

    def alterar_alocacao(self, **kwargs):
        try:
            alocacao = self._get_alocacao(**kwargs)
            if not alocacao:
                return None

            alocacao.horas = kwargs.get('horas')
            alocacao.save()

            return alocacao
        
        except Exception as err:
            raise Exception('Erro ao alterar alocação')
