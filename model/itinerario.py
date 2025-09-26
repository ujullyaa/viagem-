

Class Itinerario:
    def __init__(self, data_inicio, data_fim):

        self.__data_inicio = data_inicio
        self.__data_fim = data_fim

        @property
        def data_inicio(self):
            return self.__data_inicio

        @data_inicio.setter
        def data_inicio(self, data_inicio):
            self.data_inicio = data_inicio
        
        @property
        def data_fim(self):
            return self.__data_fim

        @data_fim.setter
        def data_fim(self, data_fim):
            self.__data_fim = data_fim
