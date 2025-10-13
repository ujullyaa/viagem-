class TelaItinerario:

    def tela_opcoes(self):
        print("-------- Itinerário ----------")
        print("Escolha a opção:")
        print("1 - Incluir Itinerário")
        print("2 - Alterar Itinerário")
        print("3 - Listar Itinerários")
        print("4 - Excluir Itinerário")
        print("0 - Retornar")

        try:
            opcao = int(input("Escolha a opção: "))
        except ValueError:
            print(" Digite um número válido!")
            opcao = -1
        return opcao

    def pega_dados_itinerario(self):
        print("\n----- Dados do Itinerário -----")
        try:
            codigo_itinerario = int(input("Código do Itinerário: "))
        except ValueError:
            print(" Código inválido, deve ser um número!")
            return None

        origem = input("Origem: ")
        destino = input("Destino: ")
        data_inicio = input("Data de Início (dd/mm/aaaa): ")
        data_fim = input("Data de Fim (dd/mm/aaaa): ")

        passagens = []
        adicionar_passagem = input("Deseja adicionar passagens a este itinerário? (s/n): ").lower()

        while adicionar_passagem == "s":
            codigo_passagem = input("  - Código da passagem: ")
            nome_passageiro = input("  - Nome do passageiro: ")
            data_passagem = input("  - Data da passagem (dd/mm/aaaa): ")
