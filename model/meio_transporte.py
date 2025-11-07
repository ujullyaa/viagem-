from model.empresa_transporte import EmpresaTransporte

class MeioTransporte:
    def __init__(self, tipo: str, capacidade: int, empresa_transporte: EmpresaTransporte):
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
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    @property
    def empresa_transporte(self):
        return self.__empresa_transporte

    @empresa_transporte.setter
    def empresa_transporte(self, empresa_transporte: EmpresaTransporte):
        self.__empresa_transporte = empresa_transporte

    def __str__(self):
        nome_empresa = (
            self.__empresa_transporte.nome_empresa if self.__empresa_transporte else "Sem empresa"
        )
        return f"{self.__tipo} ({self.__capacidade} lugares) - {nome_empresa}"
