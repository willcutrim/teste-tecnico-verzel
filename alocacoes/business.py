from alocacoes.models import Alocacao

class AlocacoesBusiness:
    model_object = Alocacao

    @property
    def alocacoes(self):
        return self.model_object

    def criar_alocacao(self, **kwargs):
        alocacao = self.alocacoes(
            projeto=kwargs.get('projeto'), 
            desenvolvedor=kwargs.get('desenvolvedor'), 
            horas=kwargs.get('horas')
        )
        alocacao.save()

        return alocacao
    
    def deletar_alocacao(self, **kwargs):
        alocacao = self.alocacoes.objects.get(id=kwargs.get('alocacao_id'))
        alocacao.delete()
