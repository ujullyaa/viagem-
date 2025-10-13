from typing import List
from model.passagem import Passagem


class Itinerario:
    def __init__(self, codigo_itinerario: int, origem: str, destino: str, data_inicio: str, data_fim: str, passagem: list[Passagem] = None):
        self.__codigo_itinerario = codigo_itinerario
        self.__origem = origem
        self.__destino = destino
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim
        self.__passagem = passagem if passagem is not None else []

    @property
    def codigo_itinerario(self):
        return self.__codigo_itinerario

    @codigo_itinerario.setter
    def codigo_itinerario(self, codigo_itinerario):
        self.__codigo_itinerario = codigo_itinerario

    @property
    def origem(self):
        return self.__origem

    @origem.setter
    def origem(self, origem):
        self.__origem = origem

    @property
    def destino(self):
        return self.__destino

    @destino.setter
    def destino(self, destino):
        self.__destino = destino

    @property
    def data_inicio(self):
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio):
        self.__data_inicio = data_inicio

    @property
    def data_fim(self):
        return self.__data_fim

    @data_fim.setter
    def data_fim(self, data_fim):
        self.__data_fim = data_fim

    @property
    def passagem(self) -> List[Passagem]:
        return self.__passagem

    @passagem.setter
    def passagem(self, passagem: list[Passagem]):
        self.__passagem = passagem

    def validar_datas(self):
        return self.__data_inicio <= self.__data_fim
