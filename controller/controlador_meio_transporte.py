from view.tela_meio_transporte import TelaMeioTransporte
from model.meio_transporte import MeioTransporte


class ControladorMeioTransporte:

    def __init__(self, controlador_controladores):
        self.__meios_transporte = []
        self.__tela_meio_transporte = TelaMeioTransporte()
        self.__controlador_controladores = controlador_controladores

    def pega_meio_por_tipo(self, tipo):
        for meio in self.__meios_transporte:
            if meio.tipo == tipo:
                return meio
        return None

    def incluir_meio_transporte(self):
        dados_meio_transporte = self.__tela_meio_transporte.pega_dados_meio_transporte()
        meio = MeioTransporte(
            dados_meio_transporte["tipo"], dados_meio_transporte["capacidade"], dados_meio_transporte["empresa"])
        self.__meios_transporte.append(meio)
        self.__tela_meio_transporte.mostra_mensagem(
            " Meio de transporte cadastrado com sucesso!")

    def lista_meios_transporte(self):
        for meio_transporte in self.__meios_transporte:
            self.__tela_meio_transporte.mostra_meio(
                {"tipo": meio_transporte.tipo, "capacidade": meio_transporte.capacidade, "empresa": meio_transporte.empresa})

    def excluir_meio_transporte(self):
        self.lista_meios_transporte()
        tipo_meio = self.__tela_meio_transporte.seleciona_meio_transporte()
        tipo = self.pega_meio_por_tipo(tipo_meio)

        if (tipo is not None):
            self.__meios_transporte.remove(tipo)
            self.lista_meios_transporte()
        else:
            self.__tela_meio_transporte.mostra_mensagem(
                "ATENCAO: Meio de Transporte não existente")

    def alterar_meio_transporte(self):
        tipo = self.__tela_meio_transporte.seleciona_meio_transporte()
        meio = self.pega_meio_por_tipo(tipo)

        if meio:
            novos_dados = self.__tela_meio_transporte.pega_dados_meio_transporte()
            meio.tipo = novos_dados["tipo"]
            meio.capacidade = novos_dados["capacidade"]
            meio.empresa = novos_dados["empresa"]
            self.__tela_meio_transporte.mostra_mensagem(
                " Meio de transporte atualizado com sucesso!")
        else:
            self.__tela_meio_transporte.mostra_mensagem(
                " Meio de transporte não encontrado.")

    def retornar(self):
        self.__controlador_controladores.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_meio_transporte, 2: self.listar_meios_transporte,
                        3: self.alterar_meio_transporte, 4: self.excluir_meio_transporte,
                        0: self.retornar}

        continua = True

        while continua:
            lista_opcoes[self.__tela_meio_transporte.tela_opcoes()]()
