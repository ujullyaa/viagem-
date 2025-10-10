from view.tela_controladores import TelaControladores
from controlador_empresa_transporte import ControladorEmpresaTransporte
from controlador_itinerario import ControladorItinerario
from controlador_meio_transporte import ControladorMeioTransporte
from controlador_passagem import ControladorPassagem
from controlador_viagem import ControladorViagem
from controlador_pessoa import ControladorPessoa
from controlador_pagamento import ControladorPagamento

class ControladorControladores:
    def __init__(self):
        self.__tela_controladores = TelaControladores()
        self.__controlador_empresa_transporte = ControladorEmpresaTransporte(self)
        self.__controlador_itinerario = ControladorItinerario(self)
        self.__controlador_meio_transporte = ControladorMeioTransporte(self)
        self.__controlador_passagem = ControladorPassagem(self)
        self.__controlador_viagem = ControladorViagem(self)
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_pagamento = ControladorPagamento(self)
    
    @property
    def controlador_empresa_transporte(self):
        return self.__controlador_empresa_transporte
    
    @property
    def controlador_itinerario(self):
        return self.__controlador_itinerario
    
    @property
    def controlador_meio_transporte(self):