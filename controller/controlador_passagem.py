from view.tela_passagem import TelaPassagem
from model.passagem import Passagem
from model.pessoa import Pessoa
from model.pagamento import Pagamento
from model.meio_transporte import MeioTransporte


class ControladorPassagem:
    def __init__(self, controlador_controladores):
        self.__passagens = []
        self.__tela_passagem = TelaPassagem()
        self.__controlador_controladores = controlador_controladores
