from Passagem import passagem

class Itinerario:
    def __init__(self, origem: str, destino: str, data_inicio: str, data_fim: str, passagem: Passagem):

        self.__origem = origem
        self.__destino = destino
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim
        self.__passagem = []


    @property
    def origem(self):
        return self.__origem

    @cidade.setter
    def origem(self, origem):
        self.__origem = origem

    @property
    def destino(self):
        return self.__destino

    @pais.setter
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
    def passagem(self):
        return self.__passagem

    def validar_datas(self):
        return self.__data_inicio <= self.__data_fim






