import FreeSimpleGUI as sg
from daos.viagem_dao import ViagemDAO
from model.viagem import Viagem
from view.tela_viagem import TelaViagem
from daos.pessoa_dao import PessoaDAO
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException

class ControladorViagem:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__dao = ViagemDAO()
        self.__tela = TelaViagem()
        self.__pessoa_dao = PessoaDAO()

    def abre_tela(self):
        opcoes = {
            1: self.cadastrar_viagem,
            2: self.listar_viagens,
            3: self.atualizar_status,
            4: self.alterar_viagem,  
            5: self.excluir_viagem,
            0: self.retornar
        }

        while True:
            opcao = self.__tela.tela_opcoes()
            
            if opcao == 0:
                break
            
            try:
                acao = opcoes.get(int(opcao))
            except (ValueError, TypeError):
                acao = None

            if acao:
                acao()
            else:
                self.__tela.mostra_mensagem("⚠️ Opção inválida.")
        
        self.retornar()

    def retornar(self):
        return

    def pega_viagem_por_codigo(self, codigo):
        for v in self.__dao.get_all():
            if str(v.codigo) == str(codigo):
                return v
        return None

    def cadastrar_viagem(self):
        try:
            dados = self.__tela.pega_dados_viagem()
            if not dados: return

            # Verifica Código Duplicado
            if self.pega_viagem_por_codigo(dados['codigo']):
                raise ElementoRepetidoException(f"Viagem com código {dados['codigo']} já existe.")

            # Valida Passageiro
            pessoa = self.__pessoa_dao.get(dados.get("cpf", ""))
            if not pessoa:
                raise ElementoNaoExisteException("Passageiro (CPF) não encontrado.")

            # Selecionar Itinerário
            ctrl_itin = self.__controlador_sistema.controlador_itinerario
            lista_itinerarios_objs = ctrl_itin.itinerarios
            
            if not lista_itinerarios_objs:
                raise ElementoNaoExisteException("Não há itinerários cadastrados.")

            cod_itinerario = self.__tela.seleciona_itinerario(lista_itinerarios_objs)
            if not cod_itinerario: return 
            
            itinerario_obj = ctrl_itin.pega_itinerario_por_codigo(cod_itinerario)

            # Selecionar Veículo
            ctrl_transporte = self.__controlador_sistema.controlador_meio_transporte
            lista_meios_objs = ctrl_transporte.meios_transporte
            
            if not lista_meios_objs:
                raise ElementoNaoExisteException("Não há veículos cadastrados.")

            veiculo_obj = self.__tela.seleciona_meio_transporte(lista_meios_objs)
            if not veiculo_obj: return 
            
            empresa_transporte_obj = veiculo_obj.empresa_transporte

            nova = Viagem(
                codigo=dados.get("codigo", ""), 
                data_partida=dados.get("data_partida", ""),
                data_chegada=dados.get("data_chegada", ""), 
                itinerario=itinerario_obj,
                meio_transporte=veiculo_obj, 
                empresa_transporte=empresa_transporte_obj,
                status="Pendente", 
                preco_base=0.0, 
                pagamento=None, 
                passageiro=pessoa
            )
            
            self.__dao.add(nova)
            self.__tela.mostra_mensagem("✔️ Viagem cadastrada com sucesso!")

        except (ElementoRepetidoException, ElementoNaoExisteException) as e:
            self.__tela.mostra_mensagem(str(e))

    def _monta_dados_listagem(self):
        viagens = self.__dao.get_all()
        dados = []
        for v in viagens:
            itin_str = v.itinerario.origem + "->" + v.itinerario.destino if v.itinerario else "N/A"
            meio_str = v.meio_transporte.tipo if v.meio_transporte else "N/A"
            
            dados.append({
                "codigo": v.codigo, 
                "data": v.data_partida, 
                "status": v.status,
                "itinerario": itin_str,
                "veiculo": meio_str
            })
        return dados

    def listar_viagens(self):
        dados = self._monta_dados_listagem()
        self.__tela.mostra_viagens(dados)

    def atualizar_status(self):
        try:
            lista = self._monta_dados_listagem()
            if not lista:
                self.__tela.mostra_mensagem("Nenhuma viagem cadastrada.")
                return

            codigo = self.__tela.seleciona_viagem(lista)
            if not codigo: return

            viagem = self.pega_viagem_por_codigo(codigo)
            if not viagem:
                raise ElementoNaoExisteException("Viagem não encontrada.")

            novo_status = self.__tela.pega_novo_status()
            if novo_status:
                viagem.status = novo_status
                self.__dao.update(viagem)
                self.__tela.mostra_mensagem("✔️ Status atualizado!")
            else:
                self.__tela.mostra_mensagem("❌ Atualização cancelada.")

        except ElementoNaoExisteException as e:
            self.__tela.mostra_mensagem(str(e))

    def alterar_viagem(self):
        try:
            lista = self._monta_dados_listagem()
            if not lista:
                self.__tela.mostra_mensagem("Nenhuma viagem cadastrada.")
                return

            codigo = self.__tela.seleciona_viagem(lista)
            if not codigo: return

            viagem = self.pega_viagem_por_codigo(codigo)
            if not viagem:
                raise ElementoNaoExisteException("Viagem não encontrada.")

            dados_atuais = {
                "data_partida": viagem.data_partida,
                "data_chegada": viagem.data_chegada,
                "cpf": viagem.passageiro.cpf if viagem.passageiro else "",
                "status": viagem.status
            }

            novos = self.__tela.pega_dados_alteracao(dados_atuais)
            if not novos:
                self.__tela.mostra_mensagem("Alteração cancelada.")
                return

            viagem.data_partida = novos.get("data_partida", "")
            viagem.data_chegada = novos.get("data_chegada", "")
            
            # Status não é alterado aqui, apenas via atualizar_status

            novo_cpf = novos.get("cpf")
            if novo_cpf != dados_atuais["cpf"]:
                novo_passageiro = self.__pessoa_dao.get(novo_cpf)
                if not novo_passageiro:
                    raise ElementoNaoExisteException("Novo passageiro (CPF) não encontrado.")
                # Se houver setter no model, faria: viagem.passageiro = novo_passageiro

            self.__dao.update(viagem)
            self.__tela.mostra_mensagem("✔️ Viagem alterada com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela.mostra_mensagem(str(e))

    def excluir_viagem(self):
        try:
            lista = self._monta_dados_listagem()
            if not lista:
                self.__tela.mostra_mensagem("Lista vazia.")
                return

            codigo = self.__tela.seleciona_viagem(lista)
            if not codigo: return

            if not self.pega_viagem_por_codigo(codigo):
                raise ElementoNaoExisteException("Viagem não encontrada para exclusão.")

            self.__dao.remove(codigo)
            self.__tela.mostra_mensagem("✔️ Viagem excluída!")

        except ElementoNaoExisteException as e:
            self.__tela.mostra_mensagem(str(e))