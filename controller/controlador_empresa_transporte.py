from view.tela_empresa_transporte import TelaEmpresaTransporte
from model.empresa_transporte import EmpresaTransporte
from daos.empresa_transporte_dao import EmpresaTransporteDAO

class ControladorEmpresaTransporte:
    def __init__(self, controlador_controladores):
        self.__empresa_dao = EmpresaTransporteDAO()
        self.__tela_empresa = TelaEmpresaTransporte()
        self.__controlador_controladores = controlador_controladores

    @property
    def empresas(self):
        return self.__empresa_dao.get_all

    def pega_empresa_por_cnpj(self, cnpj: str):
        for empresa in self.__empresa_dao.get_all:
            if empresa.cnpj == cnpj:
                return empresa
        return None

    def incluir_empresa(self):
        dados = self.__tela_empresa.pega_dados_empresa()
        if self.pega_empresa_por_cnpj(dados["cnpj"]):
            self.__tela_empresa.mostra_mensagem("Empresa já cadastrada!")
            return
        empresa = EmpresaTransporte(
            nome_empresa=dados["nome_empresa"],
            telefone=dados["telefone"],
            cnpj=dados["cnpj"]
        )
        self.__empresa_dao.add(empresa)
        self.__tela_empresa.mostra_mensagem("Empresa cadastrada com sucesso!")

    def listar_empresas(self):
        if not self.__empresa_dao.get_all:
            self.__tela_empresa.mostra_mensagem("Nenhuma empresa cadastrada.")
            return
        for empresa in self.__empresa_dao.get_all:
            self.__tela_empresa.mostra_empresa({
                "nome_empresa": empresa.nome_empresa,
                "telefone": empresa.telefone,
                "cnpj": empresa.cnpj
            })

    def excluir_empresa(self):
        cnpj = self.__tela_empresa.seleciona_empresa()
        empresa = self.pega_empresa_por_cnpj(cnpj)
        if empresa:
            self.__empresa_dao.remove(empresa)
            self.__tela_empresa.mostra_mensagem("Empresa removida com sucesso!")
        else:
            self.__tela_empresa.mostra_mensagem("Empresa não encontrada.")

    def retornar(self):
        self.__controlador_controladores.inicializa_sistema()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_empresa,
            2: self.listar_empresas,
            3: self.excluir_empresa,
            0: self.retornar
        }

        while True:
            escolha = self.__tela_empresa.tela_opcoes()
            funcao = opcoes.get(escolha)
            if funcao:
                funcao()
                if escolha == 0:
                    break
            else:
                self.__tela_empresa.mostra_mensagem("Opção inválida.")
