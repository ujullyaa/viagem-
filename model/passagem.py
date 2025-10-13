from model.pessoa import Pessoa
from model.pagamento import Pagamento
from model.meio_transporte import MeioTransporte


class Passagem:
    def __init__(
        self,
        numero: int,
        assento: str,
        data_viagem: str,
        valor: float,
        pessoa: Pessoa,
        pagamento: Pagamento,
        meio_transporte: MeioTransporte
    ):
    
        self.__numero = numero
        self.__assento = assento
        self.__data_viagem = data_viagem
        self.__valor = valor
        self.__pessoa = pessoa
        self.__pagamento = pagamento
        self.__meio_transporte = meio_transporte


    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def assento(self):
        return self.__assento

    @assento.setter
    def assento(self, assento):
        self.__assento = assento

    @property
    def data_viagem(self):
        return self.__data_viagem

    @data_viagem.setter
    def data_viagem(self, data_viagem):
        self.__data_viagem = data_viagem

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    # --- Relacionamentos ---
    @property
    def pessoa(self):
        return self.__pessoa

    @pessoa.setter
    def pessoa(self, pessoa):
        self.__pessoa = pessoa

    @property
    def pagamento(self):
        return self.__pagamento

    @pagamento.setter
    def pagamento(self, pagamento):
        self.__pagamento = pagamento

    @property
    def meio_transporte(self):
        return self.__meio_transporte

    @meio_transporte.setter
    def meio_transporte(self, meio_transporte):
        self.__meio_transporte = meio_transporte
