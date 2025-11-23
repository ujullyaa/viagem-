from controller.controlador_pessoa import ControladorPessoa
from controller.controlador_empresa_transporte import ControladorEmpresaTransporte
from controller.controlador_meio_transporte import ControladorMeioTransporte
from controller.controlador_itinerario import ControladorItinerario
from controller.controlador_passagem import ControladorPassagem
from controller.controlador_pagamento import ControladorPagamento
# --- NOVO IMPORT ---
from controller.controlador_viagem import ControladorViagem 
from view.tela_controladores import TelaControladores
import FreeSimpleGUI as sg


class ControladorControladores:
    def __init__(self):
        # --- INSTÂNCIAS DOS CONTROLADORES ---
        self.__controlador_pessoa = ControladorPessoa(self)

        self.__controlador_empresa_transporte = ControladorEmpresaTransporte(self)

        self.__controlador_meio_transporte = ControladorMeioTransporte(
            self,
            self.__controlador_empresa_transporte
        )

        self.__controlador_itinerario = ControladorItinerario(self)

        self.__controlador_passagem = ControladorPassagem(
            self,
            self.__controlador_itinerario,
            self.__controlador_pessoa,
            self.__controlador_meio_transporte
        )

        self.__controlador_pagamento = ControladorPagamento(self)

        # --- INSTANCIANDO A VIAGEM ---
        self.__controlador_viagem = ControladorViagem(self)

        # Tela principal
        self.__tela_principal = TelaControladores()

    # ------------------------------------------------------------
    #                  GETTERS PÚBLICOS (IMPORTANTE!)
    # ------------------------------------------------------------

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

    @property
    def controlador_empresa_transporte(self):
        return self.__controlador_empresa_transporte

    @property
    def controlador_meio_transporte(self):
        return self.__controlador_meio_transporte

    @property
    def controlador_itinerario(self):
        return self.__controlador_itinerario

    @property
    def controlador_passagem(self):
        return self.__controlador_passagem

    @property
    def controlador_pagamento(self):
        return self.__controlador_pagamento

    # --- GETTER DA VIAGEM ---
    @property
    def controlador_viagem(self):
        return self.__controlador_viagem

    def inicializa_sistema(self):
        while True:
            opcao = self.__tela_principal.tela_opcoes()

            if opcao == 0:
                break

            elif opcao == 1:
                self.__controlador_empresa_transporte.abre_tela()

            elif opcao == 2:
                self.__controlador_itinerario.abre_tela()

            elif opcao == 3:
                self.__controlador_meio_transporte.abre_tela()

            elif opcao == 4:
                self.__controlador_passagem.abre_tela()

            elif opcao == 5:
                self.__controlador_pessoa.abre_tela()

            elif opcao == 6:
                # --- AGORA CHAMA A TELA DE VIAGEM ---
                self.__controlador_viagem.abre_tela()

            elif opcao == 7:
                self.__controlador_pagamento.abre_tela()

            else:
                sg.popup("❌ Opção inválida!", title="Erro")