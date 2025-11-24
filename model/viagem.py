import uuid


class Viagem:
    def __init__(
        self,
        codigo: int,
        data_partida: str,
        data_chegada: str,
        itinerario: object,
        meio_transporte: object,
        empresa_transporte: object,
        status: str = "Pendente",
        preco_base: float = 0.0,
        pagamento: object = None,
        passageiro: object = None
    ):
        self.__codigo = codigo
        self.__data_partida = data_partida
        self.__data_chegada = data_chegada
        self.__status = status
        self.__preco_base = preco_base

        self.__itinerario = itinerario
        self.__meio_transporte = meio_transporte
        self.__empresa_transporte = empresa_transporte
        self.__pagamento = pagamento
        self.__passageiro = passageiro

        self.__passagens = []

    @property
    def codigo(self):
        return self.__codigo

    @property
    def data_partida(self):
        return self.__data_partida

    @property
    def data_chegada(self):
        return self.__data_chegada

    @property
    def status(self):
        return self.__status

    @property
    def passageiro(self):
        return self.__passageiro

    @property
    def itinerario(self):
        return self.__itinerario

    @data_partida.setter
    def data_partida(self, nova_data):
        self.__data_partida = nova_data

    @data_chegada.setter
    def data_chegada(self, nova_data):
        self.__data_chegada = nova_data

    @status.setter
    def status(self, novo_status):
        self.__status = novo_status

    @itinerario.setter
    def itinerario(self, novo_itinerario):
        self.__itinerario = novo_itinerario

    @property
    def meio_transporte(self):
        return self.__meio_transporte

    @meio_transporte.setter
    def meio_transporte(self, novo_meio):
        self.__meio_transporte = novo_meio

    @property
    def empresa_transporte(self):
        return self.__empresa_transporte

    @empresa_transporte.setter
    def empresa_transporte(self, nova_empresa):
        self.__empresa_transporte = nova_empresa

    @property
    def pagamento(self):
        return self.__pagamento

    @pagamento.setter
    def pagamento(self, novo_pagamento):
        self.__pagamento = novo_pagamento

    def listar_passagens(self):
        return self.__passagens

    def reservar_passagem(self, passageiro, assento):
        codigo_passagem = str(uuid.uuid4())[:8]

        passagem = {
            "codigo": codigo_passagem,
            "passageiro": passageiro,
            "assento": assento
        }

        self.__passagens.append(passagem)
        return passagem

    def cancelar_passagem(self, codigo_passagem):
        for p in self.__passagens:
            if p["codigo"] == codigo_passagem:
                self.__passagens.remove(p)
                return True
        return False

    def __repr__(self):
        return f"<Viagem codigo={self.__codigo} | Status={self.__status}>"
