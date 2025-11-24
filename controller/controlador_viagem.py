import FreeSimpleGUI as sg
from daos.viagem_dao import ViagemDAO
from model.viagem import Viagem
from view.tela_viagem import TelaViagem
from daos.pessoa_dao import PessoaDAO


class ControladorViagem:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__dao = ViagemDAO()
        self.__tela = TelaViagem()
        self.__pessoa_dao = PessoaDAO()
        # Inicialização das DAOs de relacionamento (Itinerario, MeioTransporte, etc.)
        # ...

    # ---------- LOOP PRINCIPAL ----------
    def abre_tela(self):
        opcoes = {
            1: self.cadastrar_viagem,
            2: self.listar_viagens,
            3: self.reservar_viagem,
            4: self.cancelar_passagem,
            5: self.atualizar_status,

            # 🚨 CORREÇÃO ESSENCIAL: CHAVES INVERTIDAS
            6: self.alterar_viagem,  # 6 - Alterar Viagem chama ALTERAR
            7: self.excluir_viagem  # 7 - Excluir Viagem chama EXCLUIR
        }

        while True:
            opcao = self.__tela.tela_opcoes()

            # 🛑 FECHAMENTO: Trata 'X' na janela (sg.WIN_CLOSED) e '0 - Voltar ao Menu'
            if opcao == sg.WIN_CLOSED or opcao == 0:
                break

            acao = opcoes.get(opcao)

            if acao:
                acao()
            else:
                self.__tela.mostra_mensagem("⚠️ Opção inválida.")

        self.retornar()

    def retornar(self):
        return

    # --- CADASTRAR VIAGEM (Mantido) ---
    def cadastrar_viagem(self):
        dados = self.__tela.pega_dados_viagem()
        if not dados:
            return

        pessoa = self.__pessoa_dao.get(dados.get("cpf"))
        if not pessoa:
            self.__tela.mostra_mensagem("❌ Passageiro (CPF) não encontrado.")
            return

        # Busca dos objetos de relacionamento (Itinerario, Meio, Empresa) - placeholders por enquanto
        itinerario = None
        meio_transporte = None
        empresa_transporte = None

        nova = Viagem(
            codigo=dados.get("codigo"), data_partida=dados.get("data_partida"),
            data_chegada=dados.get("data_chegada"), itinerario=itinerario,
            meio_transporte=meio_transporte, empresa_transporte=empresa_transporte,
            status="Pendente", preco_base=0.0, pagamento=None, passageiro=pessoa
        )
        self.__dao.add(nova)
        self.__tela.mostra_mensagem("✔️ Viagem cadastrada com sucesso!")

    # --- LISTAR VIAGENS (Mantido) ---
    def listar_viagens(self):
        viagens = self.__dao.get_all()
        dados = []
        for v in viagens:
            dados.append({
                "codigo": v.codigo, "data": v.data_partida, "status": v.status,
                "passagens": len(v.listar_passagens())
            })
        self.__tela.mostra_viagens(dados)

    # --- RESERVAR VIAGEM (Mantido) ---
    def reservar_viagem(self):
        codigo = self.__tela.seleciona_viagem()
        if not codigo:
            return

        viagem = self.__dao.get(codigo)
        if not viagem:
            self.__tela.mostra_mensagem("❌ Viagem não encontrada.")
            return

        assento = "A" + str(len(viagem.listar_passagens()) + 1)
        passagem = viagem.reservar_passagem(viagem.passageiro, assento)

        self.__dao.update(viagem)
        self.__tela.mostra_mensagem(
            f"✔️ Passagem reservada!\nCódigo: {passagem['codigo']}\nAssento: {assento}"
        )

    # --- CANCELAR PASSAGEM (Mantido) ---
    def cancelar_passagem(self):
        codigo = self.__tela.seleciona_viagem()
        if not codigo:
            return

        viagem = self.__dao.get(codigo)
        if not viagem:
            self.__tela.mostra_mensagem("❌ Viagem não encontrada.")
            return

        lista = viagem.listar_passagens()
        if not lista:
            self.__tela.mostra_mensagem("❌ Não há passagens nesta viagem.")
            return

        cod_pass = self.__tela.seleciona_passagem(lista)
        if not cod_pass:
            return

        if viagem.cancelar_passagem(cod_pass):
            self.__dao.update(viagem)
            self.__tela.mostra_mensagem("✔️ Passagem cancelada com sucesso!")
        else:
            self.__tela.mostra_mensagem("❌ Código da passagem não encontrado.")

    # --- ATUALIZAR STATUS (Mantido) ---
    def atualizar_status(self):
        codigo = self.__tela.seleciona_viagem()
        if not codigo:
            return

        viagem = self.__dao.get(codigo)
        if not viagem:
            self.__tela.mostra_mensagem("❌ Viagem não encontrada.")
            return

        novo_status = self.__tela.pega_novo_status()

        if novo_status:
            viagem.status = novo_status
            self.__dao.update(viagem)
            self.__tela.mostra_mensagem("✔️ Status atualizado!")
        else:
            self.__tela.mostra_mensagem("❌ Atualização de status cancelada.")

    # --- ALTERAR VIAGEM (Mantido) ---
    def alterar_viagem(self):
        codigo = self.__tela.seleciona_viagem()
        if not codigo:
            return

        viagem = self.__dao.get(codigo)
        if not viagem:
            self.__tela.mostra_mensagem("❌ Viagem não encontrada.")
            return

        dados_atuais = {
            "data_partida": viagem.data_partida,
            "data_chegada": viagem.data_chegada,
            "cpf": viagem.passageiro.cpf,
            "status": viagem.status
        }

        novos = self.__tela.pega_dados_alteracao(dados_atuais)
        if not novos:
            self.__tela.mostra_mensagem("Alteração da viagem cancelada.")
            return

        viagem.data_partida = novos.get("data_partida", viagem.data_partida)
        viagem.data_chegada = novos.get("data_chegada", viagem.data_chegada)
        viagem.status = novos.get("status", viagem.status)

        self.__dao.update(viagem)
        self.__tela.mostra_mensagem("✔️ Viagem alterada com sucesso!")

    # --- EXCLUIR VIAGEM (Mantido) ---
    def excluir_viagem(self):
        codigo = self.__tela.seleciona_viagem()
        if not codigo:
            return

        self.__dao.remove(codigo)
        self.__tela.mostra_mensagem("✔️ Viagem excluída!")
