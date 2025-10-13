

class TelaMeioTransporte:

    def tela_opcoes(self):
        print("-------- Meio de Transporte ----------")
        print("Escolha a opção:")
        print("1 - Incluir Meio de Transporte")
        print("2 - Alterar Meio de Transporte")
        print("3 - Listar Meio de Transporte")
        print("4 - Excluir Meio de Transporte")
        print("0 - Retornar")

        try:
            opcao = int(input("Escolha a opção: "))
        except ValueError:
            print(" Digite um número válido!")
            opcao = -1
        return opcao

    def pega_dados_meio_transporte(self):
        print("----- Dados do Meio de Transporte -----")
        tipo = input("Tipo do meio de transporte: ")
        try:
            capacidade = int(input("Capacidade: "))
        except ValueError:
            print(" Capacidade inválida, deve ser um número!")
            return None
        empresa = input("Empresa responsável: ")

        return {"tipo": tipo, "capacidade": capacidade, "empresa": empresa}

    def mostra_meio(self, dados_meio_transporte):
        print("\n----- Meio de Transporte -----")
        print(f"Tipo: {dados_meio_transporte['tipo']}")
        print(f"Capacidade: {dados_meio_transporte['capacidade']}")
        print(f"Empresa: {dados_meio_transporte['empresa']}")
        print("-----------------------------\n")

    def mostra_mensagem(self, msg):
        print(msg)

    def seleciona_meio_transporte(self):
        print("----- Selecionar Meio de Transporte -----")
        tipo = input("Digite o tipo do meio de transporte: ")
        return tipo
