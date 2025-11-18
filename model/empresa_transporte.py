class EmpresaTransporte:
    
    def __init__(self, nome_empresa: str, telefone: str, cnpj: str):
        self.__nome_empresa = nome_empresa
        self.__telefone = telefone
        self.__cnpj = cnpj

    @property
    def nome_empresa(self):
        return self.__nome_empresa

    @nome_empresa.setter
    def nome_empresa(self, nome_empresa: str):
        self.__nome_empresa = nome_empresa

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        self.__cnpj = cnpj

    def __str__(self):
        return f"{self.__nome_empresa} (CNPJ: {self.__cnpj})"
