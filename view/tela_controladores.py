class TelaControladores:
    def tela_opcoes(self):
        print("\n==============================")
        print("  SISTEMA DE GERENCIAMENTO DE VIAGENS")
        print("==============================")
        print("1 - Empresa de Transporte")
        print("2 - Itinerário")
        print("3 - Meio de Transporte")
        print("4 - Passagem")
        print("5 - Pessoa")
        print("6 - Viagem")
        print("7 - Pagamento")
        print("0 - Sair do Sistema")

        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número.")
            opcao = -1

        return opcao
