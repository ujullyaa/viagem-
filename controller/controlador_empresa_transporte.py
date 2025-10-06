from empresa_transporte import Empresa_transporte
from view_empresa_transporte import View_empresa_transporte


class Controlador_Empresa_Transporte:

    def __init__(self, empresa_transporte: Empresa_transporte, view_empresa_transporte: View_empresa_transporte):

        self.__empresa_transporte = empresa_transporte
        self.__view_empresa_transporte = view_empresa_transporte

    @property
    def empresa_transporte(self):
        return self.__empresa_transporte

    @property
    def view_empresa_transporte(self):
        return self.__view_empresa_transporte

    def salvar_configuracao(self, nome, cnpj, telefone):

        self.__empresa_transporte.nome_empresa = nome
        self.__empresa_transporte.cnpj = cnpj
        self.__empresa_transporte.telefone = telefone
        self.view_empresa_transporte.exibir_mensagem(
            f"Configuração salva para: {nome}")

    def exibir_informacoes(self):

        dados = {
            "Nome": self.__empresa_transporte.nome_empresa,
            "CNPJ": self.__empresa_transporte.cnpj,
            "Telefone": self.__empresa_transporte.telefone
        }
        self.view_empresa_transporte.mostrar_detalhes_empresa(dados)
