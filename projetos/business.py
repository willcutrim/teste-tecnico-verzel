from .models import Projeto


class ProjetosBusiness:
    model_object = Projeto

    @property
    def projeto(self):
        return self.model_object
    
    def _get_projeto(self, **kwargs):
        try:
            projeto = self.projeto.objects.get(id=kwargs.get('projeto_id'))
            return projeto
        
        except self.projeto.DoesNotExist:
            return None
    
    def criar_projeto(self, **kwargs):
        try:
            projeto = self.projeto(
                nome=kwargs.get('nome'),
                data_inicial=kwargs.get('data_inicial'),
                data_final=kwargs.get('data_final'),
            )
            projeto.save()

            return projeto

        except Exception as err:
            raise Exception('Erro ao criar projeto')
        
    def deletar_projeto(self, **kwargs):
        try:
            projeto = self._get_projeto(**kwargs)
            if not projeto:
                return None

            projeto.delete()

        except Exception as err:
            raise Exception('Erro ao deletar projeto')
        
    def atualizar_projeto(self, **kwargs):
        try:
            projeto = self._get_projeto(**kwargs)
            if not projeto:
                return None

            projeto.nome = kwargs.get('nome')
            projeto.data_inicial = kwargs.get('data_inicial')
            projeto.data_final = kwargs.get('data_final')
            projeto.save()

            return projeto

        except Exception as err:
            raise Exception('Erro ao atualizar projeto')