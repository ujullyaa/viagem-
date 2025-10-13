class TelaPagamento:
    def __init__(self):
        print(" ----- PAGAMENTO ----- ")

    def tela_opcoes(self):
        print("\nEscolha uma das opções abaixo:")
        print("1 - Incluir pagamento")
        print("2 - Listar pagamentos")
        print("3 - Excluir pagamento")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao in [0, 1, 2, 3]:
                    return opcao
                print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def escolhe_tipo_pagamento(self):
        print("\nEscolha a forma de pagamento:")
        print("1 - Cartão")
        print("2 - Pix")
        print("3 - Cédulas")
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    return "cartao"
                elif opcao == 2:
                    return "pix"
                elif opcao == 3:
                    return "cedulas"
                print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def pega_dados_pagamento(self):
        print("\n --- NOVO PAGAMENTO --- ")
        cpf_passageiro = input("CPF do passageiro: ")
        valor_total = float(input("Valor total: "))
        data = input("Data (DD/MM/AAAA): ")
        pagou = input("Pagamento efetuado? (s/n): ")
        forma_pagamento = self.escolhe_tipo_pagamento()
        return {
            "cpf_passageiro": cpf_passageiro,
            "valor_total": valor_total,
            "data": data,
            "pagou": pagou,
            "forma_pagamento": forma_pagamento
        }

    def pega_dados_cartao(self):
        print("\n --- DADOS CARTÃO --- ")
        numero_cartao = input("Número do cartão: ")
        nome_titular = input("Nome do titular: ")
        validade = input("Validade (MM/AA): ")
        bandeira = input("Bandeira: ")
        return {
            "numero_cartao": numero_cartao,
            "nome_titular": nome_titular,
            "validade": validade,
            "bandeira": bandeira
        }

    def pega_dados_pix(self):
        print("\n --- DADOS PIX --- ")
        chave_pix = input("Chave Pix: ")
        banco = input("Banco: ")
        return {
            "chave_pix": chave_pix,
            "banco": banco
        }

    def mostra_pagamento(self, dados_pagamento: dict):
        print("\n--- DADOS DO PAGAMENTO ---")
        print(f"Código: {dados_pagamento['codigo']}")
        print(f"Passageiro: {dados_pagamento['passageiro']}")
        print(f"Forma de Pagamento: {dados_pagamento['forma_pagamento']}")
        print(f"Valor Total: {dados_pagamento['valor_total']}")
        print(f"Data: {dados_pagamento['data']}")
        print("-----------------------------")

    def mostra_mensagem(self, msg: str):
        print(msg)

    def seleciona_pagamento(self):
        while True:
            try:
                codigo = int(input("Digite o código do pagamento: "))
                return codigo
            except ValueError:
                print("Entrada inválida. Digite um número.")
