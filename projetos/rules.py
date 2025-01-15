from .models import Projeto, Desenvolvedor

class ProjetosRules:
    model_object = Projeto

    @property
    def projeto(self):
        return self.model_object
    
    def validar_tecnologias(self, desenvolvedor: Desenvolvedor) -> bool:
        """
        Verifica se o desenvolvedor possui pelo menos uma tecnologia exigida pelo projeto.
        """
        tecnologias_projeto = set(self.projeto.tecnologias_exigidas)
        tecnologias_desenvolvedor = set(desenvolvedor.tecnologias)
        return not tecnologias_projeto.isdisjoint(tecnologias_desenvolvedor)
    
    def alocar_desenvolvedor(self, desenvolvedor: Desenvolvedor) -> bool:
        """
        Aloca um desenvolvedor ao projeto se ele passar na validação de tecnologias.
        """
        if self.validar_tecnologias(desenvolvedor):
            # Código para alocar o desenvolvedor ao projeto
            return True
        
        return False