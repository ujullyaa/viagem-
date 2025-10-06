from Empresa_transporte import empresa_transporte

Class Meio_transporte:
    def __init__(self, tipo, capacidade, empresa_transporte):

        self.__tipo = tipo
        self.__capacidade = capacidade
        self.__empresa_transporte = empresa_transporte


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
    def empresa_transporte(self):
        return self.__empresa

    @empresa.setter
    def empresa_transporte(self, empresa_transporte):
        self.__empresa = empresa






