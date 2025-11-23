from view.tela_empresa_transporte import TelaEmpresaTransporte
from model.empresa_transporte import EmpresaTransporte
from daos.empresa_transporte_dao import EmpresaTransporteDAO
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException

class ControladorEmpresaTransporte:

    def __init__(self, controlador_controladores):
        self.__empresa_dao = EmpresaTransporteDAO()
        self.__tela = TelaEmpresaTransporte()
        self.__controlador_controladores = controlador_controladores

    @property
    def empresas(self):
        return self.__empresa_dao.get_all()
    
    def __limpa_numeros(self, s: str) -> str:
        if s is None: return ""
        return ''.join(ch for ch in str(s) if ch.isdigit())

    def __validar_cnpj(self, cnpj: str) -> bool:
        c = self.__limpa_numeros(cnpj)
        return len(c) == 14

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
        if not dados: return

        try:
            cnpj_limpo = self.__limpa_numeros(dados.get("cnpj", ""))
            telefone_limpo = self.__limpa_numeros(dados.get("telefone", ""))

            if not self.__validar_cnpj(cnpj_limpo):
                self.__tela.mostra_mensagem("❌ CNPJ inválido!")
                return

            if not self.__validar_telefone(telefone_limpo):
                self.__tela.mostra_mensagem("❌ Telefone inválido!")
                return

            if self.pega_empresa_por_cnpj(cnpj_limpo):
                raise ElementoRepetidoException(f"Empresa com CNPJ {cnpj_limpo} já existe.")

            empresa = EmpresaTransporte(
                nome_empresa=dados.get("nome", "").strip(),
                telefone=telefone_limpo,
                cnpj=cnpj_limpo
            )

            self.__empresa_dao.add(empresa)
            self.__tela.mostra_mensagem("🏢 Empresa cadastrada com sucesso!")

        except ElementoRepetidoException as e:
            self.__tela.mostra_mensagem(str(e))

    def alterar_empresa(self):
        try:
            empresas = self.__empresa_dao.get_all()
            if not empresas:
                self.__tela.mostra_mensagem("Nenhuma empresa cadastrada.")
                return

            cnpj_selecionado = self.__tela.seleciona_empresa(empresas)
            if not cnpj_selecionado: return

            empresa = self.pega_empresa_por_cnpj(cnpj_selecionado)
            
            if not empresa:
                raise ElementoNaoExisteException("Empresa não encontrada.")

            dados = self.__tela.pega_dados_empresa(empresa)
            if not dados: return

            telefone_limpo = self.__limpa_numeros(dados.get("telefone", ""))

            if not self.__validar_telefone(telefone_limpo):
                self.__tela.mostra_mensagem("❌ Telefone inválido!")
                return

            empresa.nome_empresa = dados.get("nome", "").strip()
            empresa.telefone = telefone_limpo

            self.__empresa_dao.update(empresa)
            self.__tela.mostra_mensagem("🏢 Empresa alterada com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela.mostra_mensagem(str(e))

    def listar_empresas(self):
        empresas = self.__empresa_dao.get_all()
        if not empresas:
            self.__tela.mostra_mensagem("Nenhuma empresa cadastrada.")
            return
        self.__tela.mostra_empresas(empresas)

    def excluir_empresa(self):
        try:
            empresas = self.__empresa_dao.get_all()
            if not empresas:
                self.__tela.mostra_mensagem("Nenhuma empresa cadastrada.")
                return

            cnpj = self.__tela.seleciona_empresa(empresas)
            if not cnpj: return

            empresa = self.pega_empresa_por_cnpj(cnpj)
            
            if not empresa:
                raise ElementoNaoExisteException("Empresa não encontrada.")

            # --- EXCLUSÃO EM CASCATA (NOVIDADE) ---
            # Antes de excluir a empresa, remove os veículos dela
            self.__controlador_controladores.controlador_meio_transporte.excluir_veiculos_da_empresa(empresa)

            # Agora remove a empresa
            self.__empresa_dao.remove(empresa.cnpj)
            self.__tela.mostra_mensagem("Empresa e seus veículos removidos com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela.mostra_mensagem(str(e))

    def retornar(self):
        return 

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
            
            if escolha == 0:
                break
            
            funcao = opcoes.get(escolha)
            if funcao:
                funcao()
            else:
                self.__tela.mostra_mensagem("Opção inválida.")