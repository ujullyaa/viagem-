# controller/controlador_passagem.py
from view.tela_passagem import TelaPassagem
from model.passagem import Passagem
from daos.passagem_dao import PassagemDAO

class ControladorPassagem:
    def __init__(self, controlador_controladores, controlador_itinerario, controlador_pessoa, controlador_meio_transporte):
        self.__passagem_dao = PassagemDAO()
        self.__tela_passagem = TelaPassagem()
        self.__controlador_controladores = controlador_controladores
        self.__controlador_itinerario = controlador_itinerario
        self.__controlador_pessoa = controlador_pessoa
        self.__controlador_meio_transporte = controlador_meio_transporte

    def pega_passagem_por_numero(self, numero):
        numero = str(numero).zfill(6)
        for p in self.__passagem_dao.get_all():
            if p.numero == numero:
                return p
        return None

    def incluir_passagem(self):
        dados = self.__tela_passagem.pega_dados_passagem()
        if not dados:
            self.__tela_passagem.mostra_mensagem("❌ Dados inválidos.")
            return

        numero = str(dados["numero"]).zfill(6)
        if self.pega_passagem_por_numero(numero):
            self.__tela_passagem.mostra_mensagem("⚠️ Já existe uma passagem com esse número.")
            return

        self.__controlador_pessoa.listar_pessoas()
        cpf = self.__tela_passagem.seleciona_pessoa()
        pessoa = self.__controlador_pessoa.pega_pessoa_por_cpf(cpf)
        if not pessoa:
            self.__tela_passagem.mostra_mensagem("❌ Pessoa não encontrada.")
            return

        self.__controlador_meio_transporte.lista_meio_transporte()
        tipo_meio = self.__tela_passagem.seleciona_meio_transporte()
        meio_transporte = self.__controlador_meio_transporte.pega_meio_por_tipo(tipo_meio)
        if not meio_transporte:
            self.__tela_passagem.mostra_mensagem("❌ Meio de transporte não encontrado.")
            return

        self.__controlador_itinerario.listar_itinerarios()
        codigo_itinerario = self.__tela_passagem.seleciona_itinerario()
        itinerario = self.__controlador_itinerario.pega_itinerario_por_codigo(codigo_itinerario)
        if not itinerario:
            self.__tela_passagem.mostra_mensagem("❌ Itinerário não encontrado.")
            return

        passagem = Passagem(
            numero=numero,
            assento=dados["assento"],
            data_viagem=dados["data_viagem"],
            valor=dados["valor"],
            pessoa=pessoa,
            pagamento=None,
            meio_transporte=meio_transporte
        )
        self.__passagem_dao.add(passagem)
        itinerario.passagem.append(passagem)

        self.__tela_passagem.mostra_mensagem(f"✅ Passagem nº {numero} cadastrada com sucesso!")

    def listar_passagens(self):
        passagens = self.__passagem_dao.get_all()
        if not passagens:
            self.__tela_passagem.mostra_mensagem("📭 Nenhuma passagem cadastrada.")
            return

        for p in passagens:
            self.__tela_passagem.mostra_passagem({
                "numero": p.numero,
                "assento": p.assento,
                "data_viagem": p.data_viagem,
                "valor": p.valor,
                "pessoa": p.pessoa.nome,
                "meio_transporte": p.meio_transporte.tipo
            })

    def abre_tela(self):
        opcoes = {
            1: self.incluir_passagem,
            3: self.listar_passagens,
            0: self.__controlador_controladores.inicializa_sistema
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
