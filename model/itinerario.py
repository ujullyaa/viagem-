from datetime import datetime

class Itinerario:
    def __init__(self, codigo_itinerario: int, origem: str, destino: str,
                data_inicio: str, data_fim: str, passagens=None):
        self.__codigo_itinerario = codigo_itinerario
        self.__origem = origem
        self.__destino = destino
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim
        self.__passagens = passagens if passagens is not None else []

    @property
    def codigo_itinerario(self):
        return self.__codigo_itinerario

    @codigo_itinerario.setter
    def codigo_itinerario(self, codigo_itinerario: int):
        self.__codigo_itinerario = codigo_itinerario

    @property
    def origem(self):
        return self.__origem

    @origem.setter
    def origem(self, origem: str):
        self.__origem = origem

    @property
    def destino(self):
        return self.__destino

    @destino.setter
    def destino(self, destino: str):
        self.__destino = destino

    @property
    def data_inicio(self):
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio: str):
        self.__data_inicio = data_inicio

    @property
    def data_fim(self):
        return self.__data_fim

    @data_fim.setter
    def data_fim(self, data_fim: str):
        self.__data_fim = data_fim

    @property
    def passagens(self):
        return self.__passagens

    @passagens.setter
    def passagens(self, passagens: list):
        self.__passagens = passagens

    def validar_datas(self) -> bool:
        try:
            data_i = datetime.strptime(self.__data_inicio, "%d/%m/%Y")
            data_f = datetime.strptime(self.__data_fim, "%d/%m/%Y")
            return data_i <= data_f
        except ValueError:
            return False

    def adicionar_passagem(self, passagem):
        self.__passagens.append(passagem)

    def remover_passagem(self, passagem):
        if passagem in self.__passagens:
            self.__passagens.remove(passagem)

    def __repr__(self):
        return f"Itinerario({self.__codigo_itinerario}, {self.__origem} -> {self.__destino}, Passagens={len(self.__passagens)})"
