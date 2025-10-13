from view.tela_meio_transporte import TelaMeioTransporte
from model.meio_transporte import MeioTransporte


class ControladorMeioTransporte:

    def __init__(self, controlador_controladores):
        self.__meios_transporte = []
        self.__tela_meio_transporte = TelaMeioTransporte()
        self.__controlador_controladores = controlador_controladores

    def pega_meio_por_tipo(self, tipo):
        tipo = tipo.strip().lower()
        for meio in self.__meios_transporte:
            if meio.tipo.strip().lower() == tipo:
                return meio
        return None

    def incluir_meio_transporte(self):
        dados_meio_transporte = self.__tela_meio_transporte.pega_dados_meio_transporte()
        if dados_meio_transporte:
            meio = MeioTransporte(
                dados_meio_transporte["tipo"],
                dados_meio_transporte["capacidade"],
                dados_meio_transporte["empresa"]
            )
            self.__meios_transporte.append(meio)
            self.__tela_meio_transporte.mostra_mensagem(
                "Meio de transporte cadastrado com sucesso!"
            )
        else:
            self.__tela_meio_transporte.mostra_mensagem(
                "Falha ao cadastrar. Dados inválidos."
            )

    def lista_meio_transporte(self):
        if not self.__meios_transporte:
            self.__tela_meio_transporte.mostra_mensagem(
                "Nenhum meio de transporte cadastrado.")
            return

        for meio_transporte in self.__meios_transporte:
            self.__tela_meio_transporte.mostra_meio({
                "tipo": meio_transporte.tipo,
                "capacidade": meio_transporte.capacidade,
                "empresa": meio_transporte.empresa
            })

    def excluir_meio_transporte(self):
        self.lista_meio_transporte()
        tipo_meio = self.__tela_meio_transporte.seleciona_meio_transporte()
        if not tipo_meio:
            self.__tela_meio_transporte.mostra_mensagem(
                "Nenhum tipo informado.")
            return

        tipo_meio = tipo_meio.strip().lower()
        meio = self.pega_meio_por_tipo(tipo_meio)

        if meio:
            self.__meios_transporte.remove(meio)
            self.__tela_meio_transporte.mostra_mensagem(
                f"Meio de transporte '{meio.tipo}' excluído com sucesso!"
            )
        else:
            self.__tela_meio_transporte.mostra_mensagem(
                "ATENÇÃO: Meio de transporte não existente."
            )

    def alterar_meio_transporte(self):
        tipo = self.__tela_meio_transporte.seleciona_meio_transporte()
        if not tipo:
            self.__tela_meio_transporte.mostra_mensagem(
                "Nenhum tipo informado.")
            return

        meio = self.pega_meio_por_tipo(tipo)
        if meio:
            novos_dados = self.__tela_meio_transporte.pega_dados_meio_transporte()
            if novos_dados:
                meio.tipo = novos_dados["tipo"]
                meio.capacidade = novos_dados["capacidade"]
                meio.empresa = novos_dados["empresa"]
                self.__tela_meio_transporte.mostra_mensagem(
                    "Meio de transporte atualizado com sucesso!"
                )
            else:
                self.__tela_meio_transporte.mostra_mensagem(
                    "Alteração cancelada. Dados inválidos."
                )
        else:
            self.__tela_meio_transporte.mostra_mensagem(
                "ATENÇÃO: Meio de transporte não existente."
            )

    def retornar(self):
        self.__controlador_controladores.inicializa_sistema()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_meio_transporte,
            2: self.alterar_meio_transporte,
            3: self.lista_meio_transporte,
            4: self.excluir_meio_transporte,
            0: self.retornar
        }

        sair = False
        while not sair:
            opcao = self.__tela_meio_transporte.tela_opcoes()
            funcao_escolhida = opcoes.get(opcao)
            if funcao_escolhida:
                if opcao == 0:
                    sair = True
                funcao_escolhida()
            else:
                print("Opção inválida, tente novamente.")
