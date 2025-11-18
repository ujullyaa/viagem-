from view.tela_empresa_transporte import TelaEmpresaTransporte
from model.empresa_transporte import EmpresaTransporte
from daos.empresa_transporte_dao import EmpresaTransporteDAO

class ControladorEmpresaTransporte:

    def __init__(self, controlador_controladores):
        self.__empresa_dao = EmpresaTransporteDAO()
        self.__tela = TelaEmpresaTransporte()
        self.__controlador_controladores = controlador_controladores

    @property
    def empresas(self):
        return self.__empresa_dao.get_all()
    
    # limpa tudo que não for dígito: "(48) 9 9999-8888" -> "48999998888"
    def __limpa_numeros(self, s: str) -> str:
        if s is None:
            return ""
        return ''.join(ch for ch in str(s) if ch.isdigit())

    # valida CNPJ: após limpar deverá conter exatamente 14 dígitos
    def __validar_cnpj(self, cnpj: str) -> bool:
        c = self.__limpa_numeros(cnpj)
        return len(c) == 14

    # valida telefone: após limpar deverá conter exatamente 11 dígitos (DDD + 9)
    def __validar_telefone(self, telefone: str) -> bool:
        t = self.__limpa_numeros(telefone)
        return len(t) == 11


    def pega_empresa_por_cnpj(self, cnpj):
        for empresa in self.__empresa_dao.get_all():
            if str(empresa.cnpj) == str(cnpj):
                return empresa
        return None

    def incluir_empresa(self):
        dados = self.__tela.pega_dados_empresa()
        if not dados:
            self.__tela.mostra_mensagem("Operação cancelada.")
            return

        # limpar entradas
        cnpj_limpo = self.__limpa_numeros(dados.get("cnpj", ""))
        telefone_limpo = self.__limpa_numeros(dados.get("telefone", ""))

        # validações usando os valores limpos
        if not self.__validar_cnpj(cnpj_limpo):
            self.__tela.mostra_mensagem("❌ CNPJ inválido! Deve conter exatamente 14 números (apenas dígitos).")
            return

        if not self.__validar_telefone(telefone_limpo):
            self.__tela.mostra_mensagem("❌ Telefone inválido! Deve conter DDD + 9 dígitos (11 números no total).")
            return

        # verifica existência usando CNPJ limpo (consistência com DAO)
        if self.pega_empresa_por_cnpj(cnpj_limpo):
            self.__tela.mostra_mensagem("Empresa já cadastrada!")
            return

        empresa = EmpresaTransporte(
            nome_empresa=dados.get("nome", "").strip(),
            telefone=telefone_limpo,
            cnpj=cnpj_limpo
        )

        self.__empresa_dao.add(empresa)
        self.__tela.mostra_mensagem("🏢 Empresa cadastrada com sucesso!")


    def alterar_empresa(self):
        empresas = self.__empresa_dao.get_all()
        if not empresas:
            self.__tela.mostra_mensagem("Nenhuma empresa cadastrada.")
            return

        cnpj_selecionado = self.__tela.mostra_empresas(empresas)
        if not cnpj_selecionado:
            self.__tela.mostra_mensagem("Operação cancelada.")
            return

        empresa = self.pega_empresa_por_cnpj(cnpj_selecionado)
        if not empresa:
            self.__tela.mostra_mensagem("Empresa não encontrada.")
            return

        dados = self.__tela.pega_dados_empresa(empresa)
        if not dados:
            self.__tela.mostra_mensagem("Operação cancelada.")
            return

        # limpar telefone antes de validar/atribuir
        telefone_limpo = self.__limpa_numeros(dados.get("telefone", ""))

        if not self.__validar_telefone(telefone_limpo):
            self.__tela.mostra_mensagem("❌ Telefone inválido! Deve conter DDD + 9 dígitos (11 números no total).")
            return

        empresa.nome_empresa = dados.get("nome", "").strip()
        empresa.telefone = telefone_limpo

        self.__empresa_dao.update(empresa)
        self.__tela.mostra_mensagem("🏢 Empresa alterada com sucesso!")

    def listar_empresas(self):
        empresas = self.__empresa_dao.get_all()
        if not empresas:
            self.__tela.mostra_mensagem("Nenhuma empresa cadastrada.")
            return

        self.__tela.mostra_empresas(empresas)

    def excluir_empresa(self):
        empresas = self.__empresa_dao.get_all()
        if not empresas:
            self.__tela.mostra_mensagem("Nenhuma empresa cadastrada.")
            return

        cnpj = self.__tela.mostra_empresas(empresas)
        if not cnpj:
            self.__tela.mostra_mensagem("Operação cancelada.")
            return

        empresa = self.pega_empresa_por_cnpj(cnpj)
        if empresa:
            self.__empresa_dao.remove(empresa.cnpj)
            self.__tela.mostra_mensagem("Empresa removida com sucesso!")
        else:
            self.__tela.mostra_mensagem("Empresa não encontrada.")

    def retornar(self):
        self.__controlador_controladores.inicializa_sistema()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_empresa,
            2: self.alterar_empresa,
            3: self.listar_empresas,
            4: self.excluir_empresa,
            0: self.retornar
        }

        while True:
            escolha = self.__tela.tela_opcoes()
            funcao = opcoes.get(escolha)
            if funcao:
                funcao()
                if escolha == 0:
                    break
            else:
                self.__tela.mostra_mensagem("Opção inválida.")
