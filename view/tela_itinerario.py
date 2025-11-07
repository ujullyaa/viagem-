class TelaItinerario:
    def tela_opcoes(self):
        print("\n==============================")
        print("         MENU ITINERÁRIOS      ")
        print("==============================")
        print("1 - Incluir Itinerário")
        print("2 - Alterar Itinerário")
        print("3 - Listar Itinerários")
        print("4 - Excluir Itinerário")
        print("0 - Retornar ao menu anterior")
        print("==============================")

        try:
            opcao = int(input("Escolha a opção: "))
        except ValueError:
            print("\n❌ Entrada inválida! Digite um número.")
            opcao = -1
        return opcao

    def pega_dados_itinerario(self):
        print("\n----- Cadastro de Itinerário -----")

        try:
            codigo_itinerario = int(input("Código do Itinerário: "))
        except ValueError:
            print("❌ Código inválido! Deve ser um número.")
            return None

        origem = input("Origem: ").strip()
        destino = input("Destino: ").strip()
        data_inicio = input("Data de Início (dd/mm/aaaa): ").strip()
        data_fim = input("Data de Fim (dd/mm/aaaa): ").strip()

        passagens = []
        adicionar_passagem = input("Deseja adicionar passagens a este itinerário? (s/n): ").lower()

        while adicionar_passagem == "s":
            try:
                codigo_passagem = int(input("  - Código da Passagem: "))
            except ValueError:
                print("❌ Código inválido! Deve ser um número.")
                continue

            nome_passageiro = input("  - Nome do Passageiro: ").strip()
            data_passagem = input("  - Data da Passagem (dd/mm/aaaa): ").strip()

            passagens.append({
                "codigo_passagem": codigo_passagem,
                "nome_passageiro": nome_passageiro,
                "data_passagem": data_passagem
            })

            adicionar_passagem = input("Deseja adicionar outra passagem? (s/n): ").lower()

        return {
            "codigo_itinerario": codigo_itinerario,
            "origem": origem,
            "destino": destino,
            "data_inicio": data_inicio,
            "data_fim": data_fim,
            "passagem": passagens
        }

    def seleciona_itinerario(self):
        print("\n----- Selecionar Itinerário -----")
        try:
            codigo = int(input("Digite o código do Itinerário: "))
            return codigo
        except ValueError:
            print("❌ Código inválido! Deve ser um número.")
            return None

    def mostra_itinerario(self, dados_itinerario: dict):
        print("\n🧾 ----- Detalhes do Itinerário -----")
        print(f"Código: {dados_itinerario['codigo_itinerario']}")
        print(f"Origem: {dados_itinerario['origem']}")
        print(f"Destino: {dados_itinerario['destino']}")
        print(f"Data de Início: {dados_itinerario['data_inicio']}")
        print(f"Data de Fim: {dados_itinerario['data_fim']}")

        if dados_itinerario.get('passagem'):
            print("\nPassagens:")
            for p in dados_itinerario['passagem']:
                print(f"  - Código: {p['codigo_passagem']}, Passageiro: {p['nome_passageiro']}, Data: {p['data_passagem']}")
        else:
            print("\nNenhuma passagem cadastrada.")

        print("-----------------------------------")

    def mostra_mensagem(self, msg: str):
        print(f"\n{msg}\n")
