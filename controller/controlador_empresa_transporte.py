# controller/controlador_empresa_transporte.py
from view.tela_empresa_transporte import TelaEmpresaTransporte
from model.empresa_transporte import EmpresaTransporte
from daos.empresa_transporte_dao import EmpresaTransporteDAO
import re

class ControladorEmpresaTransporte:
    def __init__(self, controlador_controladores):
        self.__empresa_dao = EmpresaTransporteDAO()
        self.__tela_empresa = TelaEmpresaTransporte()
        self.__controlador_controladores = controlador_controladores

    @property
    def empresas(self):
        return self.__empresa_dao.get_all()

    # --- Funções auxiliares ---
    def pega_empresa_por_cnpj(self, cnpj):
        cnpj_limpo = self.__limpa_cnpj(cnpj)
        for empresa in self.__empresa_dao.get_all():
            if empresa.cnpj == cnpj_limpo:
                return empresa
        return None

    def __limpa_cnpj(self, cnpj):
        return re.sub(r'\D', '', cnpj)

    def __valida_cnpj(self, cnpj):
        cnpj_limpo = self.__limpa_cnpj(cnpj)
        return len(cnpj_limpo) == 14 and cnpj_limpo.isdigit()

    def __limpa_telefone(self, telefone):
        return re.sub(r'\D', '', telefone)

    def __valida_telefone(self, telefone):
        tel_limpo = self.__limpa_telefone(telefone)
        return len(tel_limpo) in (10, 11) and tel_limpo.isdigit()

    # --- CRUD ---
    def incluir_empresa(self):
        dados = self.__tela_empresa.pega_dados_empresa()
        if not dados:
            self.__tela_empresa.mostra_mensagem("Operação cancelada.")
            return
        if not dados["nome_empresa"] or not dados["cnpj"]:
            self.__tela_empresa.mostra_mensagem("Nome e CNPJ obrigatórios.")
            return
        if not self.__valida_cnpj(dados["cnpj"]):
            self.__tela_empresa.mostra_mensagem("CNPJ inválido! Deve ter 14 números.")
            return
        if dados.get("telefone") and not self.__valida_telefone(dados["telefone"]):
            self.__tela_empresa.mostra_mensagem("Telefone inválido! Deve ter 10 ou 11 números.")
            return
        if self.pega_empresa_por_cnpj(dados["cnpj"]):
            self.__tela_empresa.mostra_mensagem("Empresa já cadastrada!")
            return

        empresa = EmpresaTransporte(
            nome_empresa=dados["nome_empresa"],
            telefone=self.__limpa_telefone(dados.get("telefone", "")),
            cnpj=self.__limpa_cnpj(dados["cnpj"])
        )
        self.__empresa_dao.add(empresa)
        self.__tela_empresa.mostra_mensagem("✅ Empresa cadastrada com sucesso!")

    def listar_empresas(self):
        empresas = self.__empresa_dao.get_all()
        lista = [{"nome_empresa": e.nome_empresa, "telefone": e.telefone, "cnpj": e.cnpj} for e in empresas]
        self.__tela_empresa.mostra_empresa(lista)

    def alterar_empresa(self):
        empresas = self.__empresa_dao.get_all()
        cnpj = self.__tela_empresa.seleciona_empresa_lista(empresas)
        if not cnpj:
            self.__tela_empresa.mostra_mensagem("Operação cancelada.")
            return
        empresa = self.pega_empresa_por_cnpj(cnpj)
        if not empresa:
            self.__tela_empresa.mostra_mensagem("Empresa não encontrada.")
            return

        dados = self.__tela_empresa.pega_dados_empresa(empresa)
        if not dados:
            self.__tela_empresa.mostra_mensagem("Operação cancelada.")
            return
        if not self.__valida_cnpj(dados["cnpj"]):
            self.__tela_empresa.mostra_mensagem("CNPJ inválido!")
            return
        if dados.get("telefone") and not self.__valida_telefone(dados["telefone"]):
            self.__tela_empresa.mostra_mensagem("Telefone inválido! Deve ter 10 ou 11 números.")
            return

        empresa.nome_empresa = dados["nome_empresa"]
        empresa.telefone = self.__limpa_telefone(dados.get("telefone", ""))
        empresa.cnpj = self.__limpa_cnpj(dados["cnpj"])
        self.__empresa_dao.update(empresa)
        self.__tela_empresa.mostra_mensagem("✅ Empresa alterada com sucesso!")

    def excluir_empresa(self):
        empresas = self.__empresa_dao.get_all()
        cnpj = self.__tela_empresa.seleciona_empresa_lista(empresas)
        if not cnpj:
            self.__tela_empresa.mostra_mensagem("Operação cancelada.")
            return
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
            2: self.alterar_empresa,
            3: self.listar_empresas,
            4: self.excluir_empresa,
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
