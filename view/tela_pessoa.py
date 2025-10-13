class TelaPessoa:
    def tela_opcoes(self):
        print("\n-------- PESSOA ----------")
        print("1 - Incluir Pessoa")
        print("2 - Alterar Pessoa")
        print("3 - Listar Pessoas")
        print("4 - Excluir Pessoa")
        print("0 - Retornar")
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def pega_dados_pessoa(self):
        print("\n--- DADOS DA PESSOA ---")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        return {"nome": nome, "idade": idade, "cpf": cpf, "telefone": telefone}

    def seleciona_pessoa(self):
        cpf = input("Digite o CPF da pessoa: ")
        return cpf

    def mostra_pessoa(self, dados_pessoa: dict):
        print("\n--- DADOS DA PESSOA ---")
        print(f"Nome: {dados_pessoa['nome']}")
        print(f"Idade: {dados_pessoa['idade']}")
        print(f"CPF: {dados_pessoa['cpf']}")
        print(f"Telefone: {dados_pessoa['telefone']}")
        print("-----------------------")

    def mostra_mensagem(self, msg: str):
        print(msg)
