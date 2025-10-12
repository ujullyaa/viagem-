from view.tela_empresa_transporte import TelaEmpresaTransporte
from model.empresa_transporte import EmpresaTransporte


class ControladorEmpresaTransporte():

    def __init__(self, controlador_controladores):

        self.__empresas_transporte = []
        self.__tela_empresa_transporte = TelaEmpresaTransporte()
        self.__controlador_controladores = controlador_controladores


    def incluir_empresa(self):
        dados_empresa = self.__tela_empresa_transporte.pega_dados_empresa()
        empresa = EmpresaTransporte(dados_empresa["nome empresa"], dados_empresa["telefone"], dados_empresa["cnpj"])
        self.__empresas_transporte.append(empresa)

    def lista_empresa(self):
        for empresa_transporte in self.__empresas_transporte:
            self.__tela_empresa_transporte.mostra_empresa({"nome": empresa_transporte.nome_empresa, "telefone": empresa_transporte.telefone, "cnpj": empresa_transporte.cnpj})

    def pega_empresa_por_cnpj(self, cnpj: int):
        for empresa_transporte in self.__empresas_transporte:
            if(empresa_transporte.cnpj == cnpj):
                return empresa_transporte
        return None
    
    def alterar_empresa(self):
        self.lista_empresa()
        cnpj_empresa = self.__tela_empresa_transporte.seleciona_empresa()
        empresa = self.pega_empresa_por_cnpj(cnpj_empresa)

        if(empresa is not None):
            novos_dados_amigo = self.__tela_amigo.pega_dados_amigo()
            empresa novos_dados_["nome"]
            amigo.telefone = novos_dados_amigo["telefone"]
            amigo.cpf = novos_dados_amigo["cpf"]
            self.lista_amigos()
        else:
            self.__tela_amigo.mostra_mensagem("ATENCAO: Amigo não existente")

    def excluir_empresa(self):
        self.lista_empresa()
        cnpj_empresa = self.__tela_empresa_transporte.seleciona_empresa()
        empresa = self.pega_empresa_por_cnpj(cnpj_empresa)

        if(empresa is not None):
            self.__empresas_transporte.remove(empresa)
            self.lista_empresa()
        else:
            self.__tela_empresa_transporte.mostra_mensagem("ATENCAO: Empresa não existente")

    def retornar(self):
        self.__controlador_controladores.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_amigo, 2: self.lista_amigos, 3: self.excluir_amigo, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_empresa_transporte.tela_opcoes()]()



