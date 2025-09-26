
class Passagem:
    def __init__(self, numero:str , assento: str, data_viagem: str, valor: float):
        self.__numero = numero 
        self.__assento = assento 
        self.__data_viagem = data_viagem
        self.__valor = valor 

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