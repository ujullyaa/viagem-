from controller.controlador_viagem import ControladorViagem
from model.viagem import Viagem


class TelaViagem:
    def tela_opcoes(self):
        print("1 - Incluir Viagem")
        print("2 - Listar Viagens")
        print("3 - Reservar Viagem")
        print("4 - Cancelar Viagem")
        print("5 - Atualizar Viagem")
        print("6 - Excluir Viagem")
        print("0 - Retornar")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número.")
            return -1

    def pega_dados_viagem(self):
        print("----- DADOS DA VIAGEM -----")
        codigo = input("Código da Viagem: ")
        itinerario = input("Itinerário: ")
        data_partida = input("Data de Partida (DD/MM/AAAA): ")
        data_chegada = input("Data de Chegada (DD/MM/AAAA): ")
        meio_transporte = input("Meio de Transporte: ")
        empresa_transporte = input("Empresa de Transporte: ")
        status = input("Status (Agendada / Em andamento / Concluida ): ")
        preco_base = float(input("Preço Base: "))
        pagamento = input("Pagamento: ")
        passageiro = input("Passageiro: ")

        return {
            "codigo": codigo,
            "itinerario": itinerario,
            "data_partida": data_partida,
            "data_chegada": data_chegada,
            "meio_transporte": meio_transporte,
            "empresa_transporte": empresa_transporte,
            "status": status,
            "preco_base": preco_base,
            "pagamento": pagamento,
            "passageiro": passageiro
        }

    def mostra_viagem(self, dados: dict):
        print("\n ==== DADOS DA VIAGEM ====")
        for chave, valor in dados.items():
            print(f"{chave.capitalize()}: {valor}")
        print("-" * 30)

    def seleciona_viagem(self):
        return input("Digite o código da viagem: ")

    def mostra_mensagem(self, msg: str):
        print(msg)
