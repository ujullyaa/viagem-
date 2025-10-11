
class TelaEmpresaTransporte():
    
    def tela_opcoes(self):
        print("-------- EMPRESAS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Empresa")
        print("2 - Listar Empresas")
        print("3 - Excluir Empresa")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

  
    def pega_dados_empresa(self):
        print("-------- DADOS EMPRESA ----------")
        nome_empresa = input("Nome Empresa: ")
        telefone = input("Telefone: ")
        cnpj = input("CNPJ: ")

        return {"nome empresa": nome_empresa, "telefone": telefone, "cnpj": cnpj}


    def mostra_empresa(self, dados_empresa):
        print("NOME DA EMPRESA: ", dados_empresa["nome empresa"])
        print("TEFONE DA EMPRESA: ", dados_empresa["telefone"])
        print("CNPJ DA EMPRESA: ", dados_empresa["cnpj"])
        print("\n")


    def seleciona_empresa(self):
        cnpj = input("CNPJ da empresa que deseja selecionar: ")
        return cnpj

    def mostra_mensagem(self, msg):
        print(msg)