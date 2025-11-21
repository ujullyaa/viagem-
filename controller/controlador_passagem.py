from view.tela_passagem import TelaPassagem
from model.passagem import Passagem
from model.pagamento import Pagamento
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

    def incluir_passagem(self, itinerario_fixo=None):
        dados = self.__tela_passagem.pega_dados_passagem()
        if not dados: return

        numero = str(dados["numero"]).zfill(6)
        if self.pega_passagem_por_numero(numero):
            self.__tela_passagem.mostra_mensagem("⚠️ Já existe uma passagem com esse número.")
            return

        # 2. Seleciona Pessoa
        pessoa = self.__controlador_pessoa.escolher_pessoa_externo()
        if not pessoa:
            self.__tela_passagem.mostra_mensagem("❌ Nenhuma pessoa selecionada.")
            return

        # 3. Seleciona Meio de Transporte
        tipo_meio = self.__tela_passagem.seleciona_meio_transporte()
        if not tipo_meio: return 

        meio_transporte = self.__controlador_meio_transporte.pega_meio_por_tipo(tipo_meio)
        if not meio_transporte:
            self.__tela_passagem.mostra_mensagem(f"❌ O meio de transporte '{tipo_meio}' não foi encontrado no cadastro.")
            return

        # 4. Seleciona Itinerário (AGORA USANDO TABELA)
        itinerario = None
        if itinerario_fixo:
            itinerario = itinerario_fixo
        else:
            # --- MUDANÇA AQUI ---
            # 1. Pega a lista de objetos itinerário
            lista_objs = self.__controlador_itinerario.itinerarios
            
            # 2. Formata para dicionários simples para a View exibir
            dados_itinerarios = []
            for it in lista_objs:
                dados_itinerarios.append({
                    "codigo": it.codigo_itinerario,
                    "origem": it.origem,
                    "destino": it.destino,
                    "inicio": it.data_inicio
                })
            
            # 3. Chama a tela nova passando a lista
            codigo_itinerario = self.__tela_passagem.seleciona_itinerario(dados_itinerarios)
            
            if not codigo_itinerario:
                return # Cancelou na tela de itinerário

            itinerario = self.__controlador_itinerario.pega_itinerario_por_codigo(codigo_itinerario)
            
        if not itinerario:
            self.__tela_passagem.mostra_mensagem("❌ Itinerário não encontrado.")
            return

        # 5. Verificação de Pagamento
        pagamento_confirmado = self.__tela_passagem.confirma_pagamento_visual(dados["valor"], pessoa.nome)

        if not pagamento_confirmado:
            self.__tela_passagem.mostra_mensagem("⚠️ Pagamento pendente. Cadastro cancelado.")
            return 

        novo_pagamento = Pagamento(
            valor=float(dados["valor"]),
            tipo_pagamento="Cartão/Dinheiro",
            status="Pago"
        )

        passagem = Passagem(
            numero=numero,
            assento=dados["assento"],
            data_viagem=dados["data_viagem"],
            valor=dados["valor"],
            pessoa=pessoa,
            pagamento=novo_pagamento,
            meio_transporte=meio_transporte
        )
        
        self.__passagem_dao.add(passagem)
        itinerario.passagens.append(passagem)
        self.__controlador_itinerario.atualizar_itinerario(itinerario)

        self.__tela_passagem.mostra_mensagem(f"✅ Passagem nº {numero} emitida com sucesso!")

    def listar_passagens(self):
        passagens = self.__passagem_dao.get_all()
        if not passagens:
            self.__tela_passagem.mostra_mensagem("📭 Nenhuma passagem cadastrada.")
            return

        for p in passagens:
            status_pag = "Pago" if (p.pagamento and p.pagamento.status == "Pago") else "Pendente"
            self.__tela_passagem.mostra_passagem({
                "numero": p.numero,
                "assento": p.assento,
                "data_viagem": p.data_viagem,
                "valor": p.valor,
                "pessoa": p.pessoa.nome,
                "meio_transporte": p.meio_transporte.tipo,
                "status_pagamento": status_pag
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