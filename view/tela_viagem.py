class TelaViagem:
    def tela_opcoes(self):
        print("\n-------- Viagem ----------")
        print("1 - Incluir Viagem")
        print("2 - Listar Viagens")
        print("3 - Reservar Viagem")
        print("4 - Cancelar Viagem")
        print("5 - Atualizar Viagem")
        print("6 - Excluir Viagem")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in range(0, 7):
                    return opcao
                print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def pega_dados_viagem(self):
        print("\n--- NOVA VIAGEM ---")
        codigo = int(input("Código da viagem: "))
        data_partida = input("Data de partida (DD/MM/AAAA): ")
        data_chegada = input("Data de chegada (DD/MM/AAAA): ")
        itinerario = input("Itinerário: ")
        meio_transporte = input("Meio de transporte: ")
        empresa_transporte = input("Empresa de transporte: ")
        pagamento = input("Pagamento: ")
        cpf_pessoa = input("CPF da pessoa responsável pela viagem: ")

        return {
            "codigo": codigo,
            "data_partida": data_partida,
            "data_chegada": data_chegada,
            "itinerario": itinerario,
            "meio_transporte": meio_transporte,
            "empresa_transporte": empresa_transporte,
            "pagamento": pagamento,
            "pessoa": cpf_pessoa
        }

    def mostra_viagem(self, dados_viagem: dict):
        print("\n--- DADOS DA VIAGEM ---")
        print(f"Código: {dados_viagem['codigo']}")
        print(f"Data Partida: {dados_viagem['data_partida']}")
        print(f"Data Chegada: {dados_viagem['data_chegada']}")
        print(f"Itinerário: {dados_viagem['itinerario']}")
        print(f"Meio de Transporte: {dados_viagem['meio_transporte']}")
        print(f"Empresa de Transporte: {dados_viagem['empresa_transporte']}")
        print(f"Pagamento: {dados_viagem['pagamento']}")
        print(f"Pessoa: {dados_viagem['pessoa']}")
        print("-----------------------------")

    def seleciona_viagem(self):
        while True:
            try:
                codigo = int(input("Digite o código da viagem: "))
                return codigo
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def mostra_mensagem(self, msg: str):
        print(msg)
