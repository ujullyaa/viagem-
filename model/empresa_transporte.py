
class Empresa_transporte:  

    def __init__(self, nome_empresa, cnpj, telefone):
        
        self.__nome_empresa = nome_empresa
        self.__cnpj = cnpj
        self.__telefone = telefone

    
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



