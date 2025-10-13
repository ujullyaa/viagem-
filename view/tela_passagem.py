class TelaPassagem:
    def tela_opcoes(self):
        print("-------- Passagem ----------")
        print("1 - Incluir Passagem")
        print("2 - Alterar Passagem")
        print("3 - Listar Passagens")
        print("4 - Excluir Passagem")
        print("0 - Retornar")

        try:
            opcao = int(input("Escolha a opção: "))
        except ValueError:
            print(" Digite um número válido!")
            opcao = -1
        return opcao

    def pega_dados_passagem(self):
        print("\n----- Dados da Passagem -----")
        try:
            numero = int(input("Número da Passagem: "))
        except ValueError:
            print(" Número inválido.")
            return None

        assento = input("Assento: ")
        data_viagem = input("Data da Viagem (dd/mm/aaaa): ")

        try:
            valor = float(input("Valor da Passagem: R$ "))
        except ValueError:
            print(" Valor inválido.")
            return None

        pessoa = input("Nome do Passageiro: ")
        pagamento = input("Forma de Pagamento (cartão/dinheiro/pix): ")
        meio_transporte = input("Tipo de Meio de Transporte (ônibus/avião/navio): ")

        return {
            "numero": numero,
            "assento": assento,
            "data_viagem": data_viagem,
            "valor": valor,
            "pessoa": pessoa,
            "pagamento": pagamento,
            "meio_transporte": meio_transporte
        }

    def mostra_passagem(self, dados_passagem):
        print("\n----- Passagem -----")
        print(f"Número: {dados_passagem['numero']}")
        print(f"Assento: {dados_passagem['assento']}")
        print(f"Data: {dados_passagem['data_viagem']}")
        print(f"Valor: R$ {dados_passagem['valor']:.2f}")
        print(f"Passageiro: {dados_passagem['pessoa']}")
        print(f"Pagamento: {dados_passagem['pagamento']}")
        print(f"Transporte: {dados_passagem['meio_transporte']}")
        print("-----------------------\n")

    def mostra_mensagem(self, msg):
        print(f"\n{msg}\n")

    def seleciona_passagem(self):
        print("\n----- Selecionar Passagem -----")
        try:
            numero = int(input("Digite o número da passagem: "))
        except ValueError:
            print(" Número inválido!")
            return None
        return numero
