from view.tela_viagem import TelaViagem
from model.viagem import Viagem
from model.pessoa import Pessoa
from daos.viagem_dao import ViagemDAO
# --- IMPORTS DAS EXCEPTIONS ---
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException

class ControladorViagem:
    def __init__(self, controlador_controladores):
        self.__viagem_dao = ViagemDAO()
        self.__tela_viagem = TelaViagem()
        self.__controlador_controladores = controlador_controladores

    def pega_viagem_por_codigo(self, codigo):
        # CORREÇÃO: Adicionado () no get_all
        for viagem in self.__viagem_dao.get_all():
            if str(viagem.codigo) == str(codigo):
                return viagem
        return None

    def incluir_viagem(self):
        dados_viagem = self.__tela_viagem.pega_dados_viagem()
        if not dados_viagem: return

        try:
            # EXCEPTION: Elemento Repetido
            if self.pega_viagem_por_codigo(dados_viagem["codigo"]) is not None:
                raise ElementoRepetidoException(f"Viagem com código {dados_viagem['codigo']} já existe!")

            # Busca passageiro (opcional na sua lógica original, mas vamos validar)
            # Se a sua tela pede um CPF de 'pessoa', validamos:
            # Nota: Ajuste a chave ["pessoa"] conforme o retorno real da sua tela_viagem
            if "pessoa" in dados_viagem and dados_viagem["pessoa"]:
                cpf = dados_viagem["pessoa"]
                pessoa = self.__controlador_controladores.controlador_pessoa.pega_pessoa_por_cpf(cpf)
                
                # EXCEPTION: Elemento Não Existe
                if pessoa is None:
                    raise ElementoNaoExisteException(f"Passageiro com CPF {cpf} não encontrado.")
            else:
                # Se a lógica permitir criar sem pessoa, trate aqui
                pessoa = None 

            # Instancia Viagem (Assumindo que todos os objetos necessários venham do dados_viagem ou sejam None)
            # Nota: O model Viagem exige muitos objetos (itinerario, transporte, etc).
            # Se a tela retorna apenas strings, você precisaria buscar esses objetos nos outros controladores aqui.
            # Mantendo simples conforme seu código original:
            nova_viagem = Viagem(
                codigo=dados_viagem["codigo"],
                data_partida=dados_viagem["data_partida"],
                data_chegada=dados_viagem["data_chegada"],
                itinerario=dados_viagem.get("itinerario"),       # Cuidado: Model espera Objeto
                meio_transporte=dados_viagem.get("meio_transporte"), # Model espera Objeto
                empresa_transporte=dados_viagem.get("empresa_transporte"), # Model espera Objeto
                status="Agendada",
                preco_base=0.0, 
                pagamento=dados_viagem.get("pagamento"), # Model espera Objeto
                passageiro=pessoa
            )

            self.__viagem_dao.add(nova_viagem)
            self.__tela_viagem.mostra_mensagem("Viagem cadastrada com sucesso!")

        except (ElementoRepetidoException, ElementoNaoExisteException) as e:
            self.__tela_viagem.mostra_mensagem(str(e))

    def listar_viagens(self):
        # CORREÇÃO: Adicionado () no get_all
        viagens = self.__viagem_dao.get_all()
        if not viagens:
            self.__tela_viagem.mostra_mensagem("Nenhuma viagem cadastrada.")
            return

        # Ajuste para exibir corretamente (convertendo objetos para string se necessario)
        lista_exibicao = []
        for v in viagens:
            lista_exibicao.append({
                "codigo": v.codigo,
                "destino": v.itinerario.destino if v.itinerario else "N/A", # Exemplo de acesso seguro
                "data": v.data_partida,
                "horario": "N/A" # Seu model não tem horário separado, talvez data_partida tenha
            })
        self.__tela_viagem.mostra_viagens(lista_exibicao)

    def reservar_viagem(self):
        try:
            self.listar_viagens()
            codigo = self.__tela_viagem.seleciona_viagem()
            if not codigo: return

            viagem = self.pega_viagem_por_codigo(codigo)

            # EXCEPTION: Elemento Não Existe
            if viagem is None:
                raise ElementoNaoExisteException("Viagem não encontrada.")

            passageiro_nome = input("Nome do passageiro: ") # Ideal seria usar a tela GUI
            assento = input("Número do assento: ")
            passageiro = Pessoa(passageiro_nome, 0, "", "") 
            
            if viagem.reservar_passagem(passageiro, assento):
                self.__tela_viagem.mostra_mensagem("Reserva realizada!")
            else:
                self.__tela_viagem.mostra_mensagem("Falha ao reservar (indisponível).")

        except ElementoNaoExisteException as e:
            self.__tela_viagem.mostra_mensagem(str(e))

    def cancelar_viagem(self):
        try:
            codigo = self.__tela_viagem.seleciona_viagem()
            viagem = self.pega_viagem_por_codigo(codigo)

            if viagem is None:
                raise ElementoNaoExisteException("Viagem não encontrada.")

            # Aqui precisaria de uma GUI para pedir o número da passagem
            # Como está usando input(), vai travar a GUI, mas mantendo a lógica original:
            num_passagem = input("Número da passagem a cancelar: ") 
            
            if viagem.cancelar_passagem(num_passagem):
                self.__tela_viagem.mostra_mensagem("Passagem cancelada!")
            else:
                self.__tela_viagem.mostra_mensagem("Passagem não encontrada nesta viagem.")

        except ElementoNaoExisteException as e:
            self.__tela_viagem.mostra_mensagem(str(e))

    def atualizar_viagem(self):
        try:
            codigo = self.__tela_viagem.seleciona_viagem()
            viagem = self.pega_viagem_por_codigo(codigo)

            if not viagem:
                raise ElementoNaoExisteException("Viagem não encontrada.")

            novo_status = input("Novo status: ") # Ideal seria GUI
            viagem.atualizar_status(novo_status)
            self.__viagem_dao.update(viagem) # Faltava salvar no DAO
            self.__tela_viagem.mostra_mensagem("Status atualizado!")

        except ElementoNaoExisteException as e:
            self.__tela_viagem.mostra_mensagem(str(e))

    def excluir_viagem(self):
        try:
            codigo = self.__tela_viagem.seleciona_viagem()
            viagem = self.pega_viagem_por_codigo(codigo)

            if not viagem:
                raise ElementoNaoExisteException("Viagem não encontrada para exclusão.")

            self.__viagem_dao.remove(viagem.codigo) # Passar a chave (código), não o objeto
            self.__tela_viagem.mostra_mensagem("Viagem excluída!")

        except ElementoNaoExisteException as e:
            self.__tela_viagem.mostra_mensagem(str(e))

    def retornar(self):
        return

    def abre_tela(self):
        opcoes = {
            1: self.incluir_viagem,
            2: self.listar_viagens,
            3: self.reservar_viagem,
            4: self.cancelar_viagem,
            5: self.atualizar_viagem,
            6: self.excluir_viagem,
            0: self.retornar
        }
        while True:
            opcao = self.__tela_viagem.tela_opcoes()
            funcao = opcoes.get(opcao)
            if opcao == 0: funcao(); break
            elif funcao: funcao()
            else: self.__tela_viagem.mostra_mensagem("Opção inválida.")