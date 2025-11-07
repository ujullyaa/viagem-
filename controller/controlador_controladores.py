from controller.controlador_empresa_transporte import ControladorEmpresaTransporte
from controller.controlador_itinerario import ControladorItinerario
from controller.controlador_meio_transporte import ControladorMeioTransporte
from controller.controlador_passagem import ControladorPassagem
from controller.controlador_pessoa import ControladorPessoa
from controller.controlador_viagem import ControladorViagem
from controller.controlador_pagamento import ControladorPagamento
from view.tela_controladores import TelaControladores

class ControladorControladores:
    def __init__(self):
        self.__tela = TelaControladores()

        # Criação dos controladores — **uma única instância para cada**
        self.__controlador_empresa_transporte = ControladorEmpresaTransporte(self)
        self.__controlador_meio_transporte = ControladorMeioTransporte(
            self, self.__controlador_empresa_transporte
        )
        self.__controlador_itinerario = ControladorItinerario(self)
        self.__controlador_pessoa = ControladorPessoa(self)

        # Controlador de passagens recebe as dependências corretas
        self.__controlador_passagem = ControladorPassagem(
            controlador_controladores=self,
            controlador_itinerario=self.__controlador_itinerario,
            controlador_pessoa=self.__controlador_pessoa,
            controlador_meio_transporte=self.__controlador_meio_transporte
        )

        self.__controlador_viagem = ControladorViagem(self)
        self.__controlador_pagamento = ControladorPagamento(self)

        # Dicionário com as opções do menu principal
        self.__opcoes = {
            1: self.__controlador_empresa_transporte.abre_tela,
            2: self.__controlador_itinerario.abre_tela,
            3: self.__controlador_meio_transporte.abre_tela,
            4: self.__controlador_passagem.abre_tela,
            5: self.__controlador_pessoa.abre_tela,
            6: self.__controlador_viagem.abre_tela,
            7: self.__controlador_pagamento.abre_tela,
            0: self.encerrar_sistema
        }

    def inicializa_sistema(self):
        """Exibe o menu principal e executa a opção escolhida."""
        while True:
            opcao = self.__tela.tela_opcoes()
            funcao = self.__opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                print("\n❌ Opção inválida! Tente novamente.")

    def encerrar_sistema(self):
        print("\n✅ Sistema encerrado com sucesso.")
        exit(0)
