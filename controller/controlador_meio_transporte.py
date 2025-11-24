from view.tela_meio_transporte import TelaMeioTransporte
from model.meio_transporte import MeioTransporte
from daos.meio_transporte_dao import MeioTransporteDAO
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException

class ControladorMeioTransporte:
    def __init__(self, controlador_controladores, controlador_empresa=None):
        self.__meio_transporte_dao = MeioTransporteDAO()
        self.__tela_meio_transporte = TelaMeioTransporte()
        self.__controlador_controladores = controlador_controladores
        
        # Pega o controlador de empresas
        if hasattr(controlador_controladores, 'controlador_empresa_transporte'):
            self.__controlador_empresa = controlador_controladores.controlador_empresa_transporte
        else:
            self.__controlador_empresa = controlador_empresa

    @property
    def meios_transporte(self):
        """Retorna lista de objetos para outros controladores"""
        return self.__meio_transporte_dao.get_all()

    # Método auxiliar apenas para tipo, se necessário
    def pega_meio_por_tipo(self, tipo):
        for m in self.__meio_transporte_dao.get_all():
            if m.tipo == tipo: return m
        return None

    def incluir_meio_transporte(self):
        # 1. Verificar se há empresas para vincular
        if not self.__controlador_empresa:
            self.__tela_meio_transporte.mostra_mensagem("Erro: Módulo de Empresas não encontrado.")
            return
            
        empresas = self.__controlador_empresa.empresas
        if not empresas:
            self.__tela_meio_transporte.mostra_mensagem("Cadastre uma empresa antes de cadastrar veículos.")
            return

        # 2. Pegar Dados (Tipo, Capacidade)
        dados = self.__tela_meio_transporte.pega_dados_meio_transporte()
        if not dados: return

        try:
            if not dados["capacidade"] or int(dados["capacidade"]) <= 0:
                raise ValueError("A capacidade deve ser um número maior que zero.")

            # 3. Selecionar Empresa
            empresa_obj = self.__tela_meio_transporte.seleciona_empresa(list(empresas))
            if not empresa_obj: return

            # 4. Criar Objeto (Sem Placa, Sem Modelo, Sem Ano)
            veiculo = MeioTransporte(
                tipo=dados["tipo"], 
                capacidade=int(dados["capacidade"]), 
                empresa_transporte=empresa_obj
            )

            self.__meio_transporte_dao.add(veiculo)
            self.__tela_meio_transporte.mostra_mensagem("Veículo cadastrado com sucesso!")

        except ValueError as e:
            self.__tela_meio_transporte.mostra_mensagem(f"Erro de valor: {e}")
        except Exception as e:
            self.__tela_meio_transporte.mostra_mensagem(f"Erro inesperado: {e}")

    def alterar_meio_transporte(self):
        meios = self.__meio_transporte_dao.get_all()
        if not meios:
            self.__tela_meio_transporte.mostra_mensagem("Nenhum veículo cadastrado.")
            return

        # Tela retorna o OBJETO selecionado
        veiculo_selecionado = self.__tela_meio_transporte.seleciona_meio_transporte(meios)
        if not veiculo_selecionado: return

        # Pega novos dados
        novos_dados = self.__tela_meio_transporte.pega_dados_meio_transporte(veiculo_selecionado)
        if not novos_dados: return

        try:
            veiculo_selecionado.tipo = novos_dados["tipo"]
            veiculo_selecionado.capacidade = int(novos_dados["capacidade"])
            
            self.__meio_transporte_dao.update(veiculo_selecionado)
            self.__tela_meio_transporte.mostra_mensagem("Veículo atualizado!")
        except ValueError:
            self.__tela_meio_transporte.mostra_mensagem("Capacidade inválida.")

    def excluir_meio_transporte(self):
        meios = self.__meio_transporte_dao.get_all()
        if not meios:
            self.__tela_meio_transporte.mostra_mensagem("Vazio.")
            return

        veiculo_selecionado = self.__tela_meio_transporte.seleciona_meio_transporte(meios)
        if not veiculo_selecionado: return

        self.__meio_transporte_dao.remove(veiculo_selecionado)
        self.__tela_meio_transporte.mostra_mensagem("Veículo excluído!")

    def lista_meio_transporte(self):
        self.__tela_meio_transporte.lista_meios(self.__meio_transporte_dao.get_all())

    def excluir_veiculos_da_empresa(self, empresa_alvo):
        # Remove veículos se a empresa for deletada
        veiculos = list(self.__meio_transporte_dao.get_all())
        count = 0
        for v in veiculos:
            if v.empresa_transporte and v.empresa_transporte.cnpj == empresa_alvo.cnpj:
                self.__meio_transporte_dao.remove(v)
                count += 1
        if count > 0:
            print(f"{count} veículos removidos automaticamente.")

    def retornar(self):
        return

    def abre_tela(self):
        opcoes = {
            1: self.incluir_meio_transporte,
            2: self.alterar_meio_transporte,
            3: self.lista_meio_transporte,
            4: self.excluir_meio_transporte,
            0: self.retornar
        }
        while True:
            opcao = self.__tela_meio_transporte.tela_opcoes()
            if opcao == 0: break
            
            funcao = opcoes.get(opcao)
            if funcao: funcao()
            else: self.__tela_meio_transporte.mostra_mensagem("Opção inválida.")