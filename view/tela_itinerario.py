
class TelaItinerario:

    def tela_opcoes(self):
        print("\n-------- Itinerário ----------")
        print("Escolha a opção:")
        print("1 - Incluir Itinerário")
        print("2 - Alterar Itinerário")
        print("3 - Listar Itinerários")
        print("4 - Excluir Itinerário")
        print("0 - Retornar")

        try:
            opcao = int(input("Escolha a opção: "))
        except ValueError:
            print("Digite um número válido!")
            opcao = -1
        return opcao

    def pega_dados_itinerario(self):
        print("\n----- Dados do Itinerário -----")
        try:
            codigo_itinerario = int(input("Código do Itinerário: "))
        except ValueError:
            print("Código inválido, deve ser um número!")
            return None

        origem = input("Origem: ")
        destino = input("Destino: ")
        data_inicio = input("Data de Início (dd/mm/aaaa): ")
        data_fim = input("Data de Fim (dd/mm/aaaa): ")

        passagens = []
        adicionar_passagem = input(
            "Deseja adicionar passagens a este itinerário? (s/n): ").lower()

        while adicionar_passagem == "s":
            try:
                codigo_passagem = int(input("  - Código da passagem: "))
            except ValueError:
                print("  Código inválido, deve ser um número!")
                continue

            nome_passageiro = input("  - Nome do passageiro: ")
            data_passagem = input("  - Data da passagem (dd/mm/aaaa): ")

            passagens.append({
                "codigo_passagem": codigo_passagem,
                "nome_passageiro": nome_passageiro,
                "data_passagem": data_passagem
            })

            adicionar_passagem = input(
                "Deseja adicionar outra passagem? (s/n): ").lower()

        return {
            "codigo_itinerario": codigo_itinerario,
            "origem": origem,
            "destino": destino,
            "data_inicio": data_inicio,
            "data_fim": data_fim,
            "passagem": passagens
        }

    def seleciona_itinerario(self):
        try:
            codigo = int(input("Digite o código do itinerário: "))
            return codigo
        except ValueError:
            print("Código inválido, deve ser um número!")
            return None

    def mostra_itinerario(self, dados_itinerario: dict):
        print("\n--- DADOS DO ITINERÁRIO ---")
        print(f"Código: {dados_itinerario['codigo_itinerario']}")
        print(f"Origem: {dados_itinerario['origem']}")
        print(f"Destino: {dados_itinerario['destino']}")
        print(f"Data de Início: {dados_itinerario['data_inicio']}")
        print(f"Data de Fim: {dados_itinerario['data_fim']}")
        if dados_itinerario['passagem']:
            print("Passagens:")
            for p in dados_itinerario['passagem']:
                print(
                    f"  Código: {p['codigo_passagem']}, Passageiro: {p['nome_passageiro']}, Data: {p['data_passagem']}")
        else:
            print("Nenhuma passagem cadastrada.")
        print("-----------------------------")

    def mostra_mensagem(self, msg: str):
        print(msg)
