from typing import List

class EmpresaTransporte:  
    def __init__(self, nome_empresa: str, cnpj: int, telefone: int):
        self.__nome_empresa = nome_empresa
        self.__cnpj = cnpj
        self.__telefone = telefone
        self.__meios_transporte: List = []  # lista de objetos MeioTransporte

    @property
    def nome_empresa(self):
        return self.__nome_empresa

    @nome_empresa.setter
    def nome_empresa(self, nome_empresa):
        self.__nome_empresa = nome_empresa

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def meios_transporte(self):
        return self.__meios_transporte

    def adicionar_meio_transporte(self, meio_transporte):
        if meio_transporte not in self.__meios_transporte:
            self.__meios_transporte.append(meio_transporte)
            # Faz o vínculo bidirecional
            meio_transporte.empresa_transporte = self

    def remover_meio_transporte(self, meio_transporte):
        if meio_transporte in self.__meios_transporte:
            self.__meios_transporte.remove(meio_transporte)
            meio_transporte.empresa_transporte = None

    def __str__(self):
        return f"{self.__nome_empresa} (CNPJ: {self.__cnpj}) - {len(self.__meios_transporte)} meios de transporte"
