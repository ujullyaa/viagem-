

class Itinerario:
    def __init__(self, cidade, pais, data_inicio, data_fim):

        self.__cidade = cidade
        self.__pais = pais
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim


        @property
        def cidade(self):
            return self.__cidade

        @cidade.setter
        def cidade(self, cidade):
            self.__cidade = cidade

        @property
        def pais(self):
            return self.__pais

        @pais.setter
        def pais(self, pais):
            self.__pais = pais
            
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


