from controller.controlador_pessoa import ControladorPessoa
from model.pessoa import Pessoa



class TelaPessoa:
    def tela_opcoes(self):
        print("----- PESSOAS -----")
        print("1. Incluir Pessoa")
        print("2. Alterar Pessoas")
        print("3. Listar Pessoa")
        print("4. Excluir Pessoa")
        print("0. Retornar")
        
        while True:
            try:
             opcao = int(input("Escolha uma opção: "))
             if opcao in [0, 1, 2, 3, 4]:
                 return opcao
             else:
                 print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    def pega_dados_pessoa(self):
        print("----- DADOS DA PESSOA -----")
        nome = input("Nome: ")
        idade = input("Idade: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        return {"nome": nome, "idade": idade, "cpf": cpf, "telefone": telefone}
    
    def mostra_pessoas(self, dados_pessoas):
        print("NOME:", dados_pessoas["nome"])
        print("IDADE:", dados_pessoas["idade"])
        print("CPF:", dados_pessoas["cpf"])
        print("TELEFONE:", dados_pessoas["telefone"])
        print("-------------------------")

    def seleciona_pessoa(self):
        cpf = input("Digite o CPF da pessoa: ")
        return cpf
    
    def mostra_mensagem(self, msg):
        print(msg)