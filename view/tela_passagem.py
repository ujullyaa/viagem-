class TelaPassagem:
    def tela_opcoes(self):
        print("\n==============================")
        print("         MENU PASSAGENS        ")
        print("==============================")
        print("1 - Incluir Passagem")
        print("2 - Alterar Passagem")
        print("3 - Listar Passagens")
        print("4 - Excluir Passagem")
        print("0 - Retornar ao menu anterior")
        print("==============================")

        try:
            opcao = int(input("Escolha a opção: "))
        except ValueError:
            print("\n❌ Entrada inválida! Digite um número.")
            opcao = -1
        return opcao

    def pega_dados_passagem(self):
        print("\n----- Cadastro de Passagem -----")

        try:
            numero = int(input("Número da Passagem: "))
        except ValueError:
            print("❌ Número inválido.")
            return None

        assento = input("Assento: ").strip()
        data_viagem = input("Data da Viagem (dd/mm/aaaa): ").strip()

        try:
            valor = float(input("Valor da Passagem (R$): "))
        except ValueError:
            print("❌ Valor inválido.")
            return None

        pessoa = input("Nome do Passageiro: ").strip()
        pagamento = input("Forma de Pagamento (Cartão / Dinheiro / Pix): ").strip()
        meio_transporte = input("Tipo de Transporte (Ônibus / Avião / Navio): ").strip()

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
        print("\n🧾 ----- Detalhes da Passagem -----")
        print(f"Número: {dados_passagem['numero']}")
        print(f"Assento: {dados_passagem['assento']}")
        print(f"Data da Viagem: {dados_passagem['data_viagem']}")
        print(f"Valor: R$ {dados_passagem['valor']:.2f}")
        print(f"Passageiro: {dados_passagem['pessoa']}")
        print(f"Pagamento: {dados_passagem['pagamento']}")
        print(f"Meio de Transporte: {dados_passagem['meio_transporte']}")
        print("-----------------------------------")

    def mostra_mensagem(self, msg):
        print(f"\n{msg}\n")

    def seleciona_passagem(self):
        print("\n----- Selecionar Passagem -----")
        try:
            numero = int(input("Digite o número da passagem: "))
            return numero
        except ValueError:
            print("❌ Número inválido.")
            return None
