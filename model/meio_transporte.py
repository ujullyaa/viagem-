from empresa_transporte import Empresa_transporte

Class Meio_transporte:
    def __init__(self, tipo, capacidade, empresa_transporte):

        self.__tipo = tipo
        self.__capacidade = capacidade
        self.__empresa = empresa_transporte


    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def capacidade(self):
        return self.__capacidade 

    @capacidade.setter
    def capacidade(self, caapacidade):
        self.__capacidade = capacidade
    
    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, empresa):
        self.__empresa = empresa




