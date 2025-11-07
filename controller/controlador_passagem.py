from view.tela_passagem import TelaPassagem
from model.passagem import Passagem
from model.pessoa import Pessoa
from model.meio_transporte import MeioTransporte

class ControladorPassagem:
    def __init__(self, controlador_controladores, controlador_itinerario, controlador_pessoa, controlador_meio_transporte):
        self.__passagens: list[Passagem] = []
        self.__tela_passagem = TelaPassagem()
        self.__controlador_controladores = controlador_controladores
        self.__controlador_itinerario = controlador_itinerario
        self.__controlador_pessoa = controlador_pessoa
        self.__controlador_meio_transporte = controlador_meio_transporte

    def pega_passagem_por_numero(self, numero: int) -> Passagem | None:
        for passagem in self.__passagens:
            if passagem.numero == numero:
                return passagem
        return None

    def incluir_passagem(self):
        dados = self.__tela_passagem.pega_dados_passagem()
        if not dados:
            self.__tela_passagem.mostra_mensagem("❌ Dados inválidos.")
            return

        if self.pega_passagem_por_numero(dados["numero"]):
            self.__tela_passagem.mostra_mensagem("⚠️ Já existe uma passagem com esse número.")
            return

        # Seleciona a pessoa
        self.__controlador_pessoa.listar_pessoas()
        cpf = self.__tela_passagem.seleciona_pessoa()
        pessoa = self.__controlador_pessoa.pega_pessoa_por_cpf(cpf)
        if not pessoa:
            self.__tela_passagem.mostra_mensagem("❌ Pessoa não encontrada.")
            return

        # Seleciona o meio de transporte
        self.__controlador_meio_transporte.lista_meio_transporte()
        tipo_meio = self.__tela_passagem.seleciona_meio_transporte()
        meio_transporte = self.__controlador_meio_transporte.pega_meio_por_tipo(tipo_meio)
        if not meio_transporte:
            self.__tela_passagem.mostra_mensagem("❌ Meio de transporte não encontrado.")
            return

        # Seleciona o itinerário
        self.__controlador_itinerario.listar_itinerarios()
        codigo_itinerario = self.__tela_passagem.seleciona_itinerario()
        itinerario = self.__controlador_itinerario.pega_itinerario_por_codigo_itinerario(codigo_itinerario)
        if not itinerario:
            self.__tela_passagem.mostra_mensagem("❌ Itinerário não encontrado.")
            return

        # Cria a passagem
        nova_passagem = Passagem(
            numero=dados["numero"],
            assento=dados["assento"],
            data_viagem=dados["data_viagem"],
            valor=dados["valor"],
            pessoa=pessoa,
            pagamento=None,  # pode conectar pagamento depois
            meio_transporte=meio_transporte
        )

        # Adiciona a passagem nas listas corretas
        self.__passagens.append(nova_passagem)
        itinerario.passagem.append(nova_passagem)

        self.__tela_passagem.mostra_mensagem("✅ Passagem cadastrada com sucesso!")

    def listar_passagens(self):
        if not self.__passagens:
            self.__tela_passagem.mostra_mensagem("📭 Nenhuma passagem cadastrada.")
            return

        for passagem in self.__passagens:
            self.__tela_passagem.mostra_passagem({
                "numero": passagem.numero,
                "assento": passagem.assento,
                "data_viagem": passagem.data_viagem,
                "valor": passagem.valor,
                "pessoa": passagem.pessoa.nome if isinstance(passagem.pessoa, Pessoa) else "N/A",
                "meio_transporte": passagem.meio_transporte.tipo if isinstance(passagem.meio_transporte, MeioTransporte) else "N/A"
            })

    def alterar_passagem(self):
        if not self.__passagens:
            self.__tela_passagem.mostra_mensagem("📭 Nenhuma passagem para alterar.")
            return

        numero = self.__tela_passagem.seleciona_passagem()
        passagem = self.pega_passagem_por_numero(numero)
        if not passagem:
            self.__tela_passagem.mostra_mensagem("❌ Passagem não encontrada.")
            return

        dados = self.__tela_passagem.pega_dados_passagem()
        if not dados:
            self.__tela_passagem.mostra_mensagem("❌ Dados inválidos.")
            return

        # Atualiza dados básicos
        passagem.numero = dados["numero"]
        passagem.assento = dados["assento"]
        passagem.data_viagem = dados["data_viagem"]
        passagem.valor = dados["valor"]

        # Atualiza pessoa
        self.__controlador_pessoa.listar_pessoas()
        cpf = self.__tela_passagem.seleciona_pessoa()
        pessoa = self.__controlador_pessoa.pega_pessoa_por_cpf(cpf)
        if pessoa:
            passagem.pessoa = pessoa

        # Atualiza meio de transporte
        self.__controlador_meio_transporte.lista_meio_transporte()
        tipo_meio = self.__tela_passagem.seleciona_meio_transporte()
        meio_transporte = self.__controlador_meio_transporte.pega_meio_por_tipo(tipo_meio)
        if meio_transporte:
            passagem.meio_transporte = meio_transporte

        self.__tela_passagem.mostra_mensagem("✅ Passagem alterada com sucesso!")

    def excluir_passagem(self):
        if not self.__passagens:
            self.__tela_passagem.mostra_mensagem("📭 Nenhuma passagem para excluir.")
            return

        self.listar_passagens()
        numero = self.__tela_passagem.seleciona_passagem()
        passagem = self.pega_passagem_por_numero(numero)
        if not passagem:
            self.__tela_passagem.mostra_mensagem("❌ Passagem não encontrada.")
            return

        # Remove passagem do itinerário
        for itinerario in self.__controlador_itinerario.itinerarios:
            if passagem in itinerario.passagem:
                itinerario.passagem.remove(passagem)

        # Remove da lista principal
        self.__passagens.remove(passagem)
        self.__tela_passagem.mostra_mensagem("🗑️ Passagem excluída com sucesso!")

    def retornar(self):
        self.__controlador_controladores.inicializa_sistema()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_passagem,
            2: self.alterar_passagem,
            3: self.listar_passagens,
            4: self.excluir_passagem,
            0: self.retornar
        }

        while True:
            escolha = self.__tela_passagem.tela_opcoes()
            funcao = opcoes.get(escolha)
            if funcao:
                funcao()
            else:
                self.__tela_passagem.mostra_mensagem("❌ Opção inválida!")

            if escolha == 0:
                break
