from view.tela_passagem import TelaPassagem
from model.passagem import Passagem
from model.pagamento import Cedula
from daos.passagem_dao import PassagemDAO
from datetime import datetime
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException

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

    # --- Método auxiliar para formatar dados para a tabela ---
    def __monta_lista_passagens(self):
        passagens = self.__passagem_dao.get_all()
        lista = []
        for p in passagens:
            lista.append({
                "numero": p.numero,
                "pessoa": p.pessoa.nome if p.pessoa else "Desconhecido",
                "data": p.data_viagem,
                "assento": p.assento,
                "valor": p.valor
            })
        return lista

    def incluir_passagem(self, itinerario_fixo=None):
        try:
            dados = self.__tela_passagem.pega_dados_passagem()
            if not dados: return

            numero = str(dados["numero"]).zfill(6)
            
            if self.pega_passagem_por_numero(numero):
                raise ElementoRepetidoException(f"Passagem número {numero} já existe.")

            # Seleciona Pessoa
            pessoa = self.__controlador_pessoa.escolher_pessoa_externo()
            if not pessoa: return 

            # Seleciona Meio de Transporte
            tipo_meio = self.__tela_passagem.seleciona_meio_transporte()
            if not tipo_meio: return 

            meio_transporte = self.__controlador_meio_transporte.pega_meio_por_tipo(tipo_meio)
            if not meio_transporte:
                raise ElementoNaoExisteException(f"O meio de transporte '{tipo_meio}' não foi encontrado.")

            # Seleciona Itinerário
            itinerario = None
            if itinerario_fixo:
                itinerario = itinerario_fixo
            else:
                lista_objs = self.__controlador_itinerario.itinerarios
                dados_itinerarios = [{"codigo": it.codigo_itinerario, "origem": it.origem, "destino": it.destino, "inicio": it.data_inicio} for it in lista_objs]
                
                codigo_itinerario = self.__tela_passagem.seleciona_itinerario(dados_itinerarios)
                if not codigo_itinerario: return 

                itinerario = self.__controlador_itinerario.pega_itinerario_por_codigo(codigo_itinerario)
            
            if not itinerario:
                raise ElementoNaoExisteException("Itinerário não encontrado.")

            # Pagamento
            pagamento_confirmado = self.__tela_passagem.confirma_pagamento_visual(dados["valor"], pessoa.nome)
            if not pagamento_confirmado:
                self.__tela_passagem.mostra_mensagem("Pagamento pendente. Cadastro cancelado.")
                return 

            novo_pagamento = Cedula(
                forma_pagamento="Dinheiro",
                pagou=True,
                data=datetime.now().strftime("%d/%m/%Y"),
                valor_total=float(dados["valor"]),
                passageiro=pessoa
            )

            passagem = Passagem(numero, dados["assento"], dados["data_viagem"], dados["valor"], pessoa, novo_pagamento, meio_transporte)
            
            self.__passagem_dao.add(passagem)
            itinerario.passagens.append(passagem)
            self.__controlador_itinerario.atualizar_itinerario(itinerario)

            self.__tela_passagem.mostra_mensagem(f"Passagem nº {numero} emitida com sucesso!")

        except (ElementoRepetidoException, ElementoNaoExisteException) as e:
            self.__tela_passagem.mostra_mensagem(str(e))
        except ValueError:
            self.__tela_passagem.mostra_mensagem("Erro: Valor deve ser numérico.")

    def alterar_passagem(self):
        try:
            # 1. Pega lista formatada
            lista_dados = self.__monta_lista_passagens()
            if not lista_dados:
                self.__tela_passagem.mostra_mensagem("Nenhuma passagem cadastrada.")
                return

            # 2. Abre tabela para selecionar
            numero = self.__tela_passagem.seleciona_passagem_por_lista(lista_dados)
            if not numero: return

            # 3. Busca objeto
            passagem = self.pega_passagem_por_numero(numero)
            if not passagem:
                raise ElementoNaoExisteException("Passagem não encontrada.")

            # 4. Abre formulário com dados preenchidos
            novos_dados = self.__tela_passagem.pega_dados_passagem(passagem)
            if not novos_dados: return

            # 5. Atualiza
            passagem.assento = novos_dados["assento"]
            passagem.data_viagem = novos_dados["data_viagem"]
            passagem.valor = novos_dados["valor"]
            
            self.__passagem_dao.update(passagem)
            self.__tela_passagem.mostra_mensagem("Passagem alterada com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela_passagem.mostra_mensagem(str(e))

    def excluir_passagem(self):
        try:
            lista_dados = self.__monta_lista_passagens()
            if not lista_dados:
                self.__tela_passagem.mostra_mensagem("Nenhuma passagem cadastrada.")
                return

            numero = self.__tela_passagem.seleciona_passagem_por_lista(lista_dados)
            if not numero: return

            passagem = self.pega_passagem_por_numero(numero)
            if not passagem:
                raise ElementoNaoExisteException("Passagem não encontrada.")

            self.__passagem_dao.remove(passagem.numero)
            self.__tela_passagem.mostra_mensagem("Passagem excluída com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela_passagem.mostra_mensagem(str(e))

    def listar_passagens(self):
        passagens = self.__passagem_dao.get_all()
        if not passagens:
            self.__tela_passagem.mostra_mensagem("Nenhuma passagem cadastrada.")
            return

        for p in passagens:
            status_pag = "Pendente"
            if p.pagamento and hasattr(p.pagamento, 'pagou') and p.pagamento.pagou:
                status_pag = "Pago"

            self.__tela_passagem.mostra_passagem({
                "numero": p.numero,
                "assento": p.assento,
                "data_viagem": p.data_viagem,
                "valor": p.valor,
                "pessoa": p.pessoa.nome,
                "meio_transporte": p.meio_transporte.tipo,
                "status_pagamento": status_pag
            })

    def retornar(self):
        return

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
            
            if escolha == 0:
                break
            elif funcao:
                funcao()
            else:
                self.__tela_passagem.mostra_mensagem("Opção inválida!")