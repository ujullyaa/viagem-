from model.empresa_transporte import EmpresaTransporte

class MeioTransporte:
    def __init__(self, tipo: str, capacidade: int, empresas_transporte: str):

        self.__tipo = tipo
        self.__capacidade = capacidade
        self.__empresa_transporte = []

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
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    @property
    def empresa(self):
        return self.__empresa_transporte

    @empresa.setter
    def empresa(self, empresa_transporte):
        self.__empresa_transporte = empresa_transporte


