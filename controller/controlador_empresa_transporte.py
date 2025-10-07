from model.empresa_transporte import Empresa_transporte


class Controlador_Empresa_Transporte:

    def __init__(self, empresas_transporte: list, tela_empresa_transporte: Tela_empresa_transporte):

        self.__empresas_transporte = []
        self.__tela_empresa_transporte = tela_empresa_transporte

    @property
    def empresas_transporte(self):
        return self.__empresas_transporte

    @property
    def view_empresa_transporte(self):
        return self.__Tela_empresa_transporte

    def salvar_configuracao(self, nome, cnpj, telefone):

        self.__empresas_transporte.nome_empresa = nome
        self.__empresas_transporte.cnpj = cnpj
        self.__empresas_transporte.telefone = telefone
        self.__tela_empresa_transporte.exibir_mensagem(
            f"Configuração salva para: {nome}")

    def exibir_informacoes(self):

        dados = {
            "Nome": self.__empresas_transporte.nome_empresa,
            "CNPJ": self.__empresas_transporte.cnpj,
            "Telefone": self.__empresas_transporte.telefone
        }
        self.__tela_empresa_transporte.mostrar_detalhes_empresa(dados)




