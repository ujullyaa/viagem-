from controller.controlador_pessoa import ControladorPessoa
from model.pessoa import Pessoa
import os
import time


class TelaPessoa:
    def __init__(self):
        self.__controlador = ControladorPessoa

    def limpar_tela(self):
        os.system('clear')

    def mostrar_titulo(self, titulo):
        print("=" * 40)
        print(f"{titulo.center(40)}")
        print("=" * 40)

    def exibir_pessoas(self):
        self.limpar_tela()
        self.mostrar_titulo("LISTA DE PESSAOS")
        pessoas = self.__controlador.listar_pessoas()
        if not pessoas:
            print("Nenhuma pessoa cadastrada.")
        else:
            for p in pessoas:
                print(f"Nome: {p.nome}")
                print(f"Idade: {p.idade}")
                print(f"CPF: {p.cpf}")
                print(f"Telefone: {p.telefone}")
                print("-" * 40)

        input("\nPresisone Enter para voltar ao menu...")

    def cadastrar_pessoa(self):
        self.limpar_tela()
        self.mostrar_titulo("CADASTRAR PESSOA")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        try:
            self.__controlador.incluir_pessoa(nome, idade, cpf, telefone)
            print("\nPessoa cadastrada com sucesso!")
        except ValueError as e:
            print(f"\n erro ao cadastrar pessoa: {e}")
        time.sleep(2)

    def menu(self):
        while True:
            self.limpar_tela()
            self.mostrar_titulo("MENU PESSOA")
            print("1- Cadastrar Pessoa")
            print("2- Listar Pessoas")
            print("0- Sair")
            print("=" * 40)

            opcao = input("Escolha uma opcao: ")

            if opcao == "1":
                self.cadastrar_pessoa()
            elif opcao == "2":
                self.exibir_pessoas()
            elif opcao == "0":
                print("\nVoltando ao menu principal...")
                time.sleep(1)
                break
            else:
                print("\nOpcao invalida! Tente novamente.")
                time.sleep(1)


if __name__ == "__main__":
    TelaPessoa().menu()
