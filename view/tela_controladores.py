class TelaControladores:
    def __init__(self):
        print("\nSistema de Gerenciamento de Viagens")
        print("Escolha uma das opções abaixo:")

    def tela_opcoes(self):
        print("1. Empresa de Transporte")
        print("2. Itinerário")
        print("3. Meio de Transporte")
        print("4. Passagem")
        print("5. Pessoa")
        print("6. Viagem")
        print("7. Pagamento")
        print("0. Sair do Sistema")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número.")
            opcao = -1
        return opcao
