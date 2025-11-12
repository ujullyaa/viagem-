import FreeSimpleGUI as sg

class TelaEmpresaTransporte:
    def __init__(self):
        sg.theme("BluePurple") 

    def tela_opcoes(self):
        layout = [
            [sg.Text("-------- EMPRESAS ----------", font=("Arial", 14, "bold"))],
            [sg.Text("Escolha a opção:")],
            [sg.Button("1 - Incluir Empresa"), 
             sg.Button("2 - Listar Empresas"), 
             sg.Button("3 - Excluir Empresa"), 
             sg.Button("0 - Retornar")],
        ]

        janela = sg.Window("Menu Empresa Transporte", layout)
        evento, _ = janela.read()
        janela.close()

        if evento is None or evento == "0 - Retornar":
            return 0
        elif evento == "1 - Incluir Empresa":
            return 1
        elif evento == "2 - Listar Empresas":
            return 2
        elif evento == "3 - Excluir Empresa":
            return 3
        else:
            return -1

    def pega_dados_empresa(self):
        layout = [
            [sg.Text("-------- DADOS EMPRESA ----------", font=("Arial", 14, "bold"))],
            [sg.Text("Nome Empresa:", size=(15, 1)), sg.Input(key="nome_empresa")],
            [sg.Text("Telefone:", size=(15, 1)), sg.Input(key="telefone")],
            [sg.Text("CNPJ:", size=(15, 1)), sg.Input(key="cnpj")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]

        janela = sg.Window("Cadastro de Empresa", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            return valores
        return None

    def mostra_empresa(self, dados_empresa):
        layout = [
            [sg.Text("-------- EMPRESA ----------", font=("Arial", 14, "bold"))],
            [sg.Text(f"Nome: {dados_empresa['nome_empresa']}")],
            [sg.Text(f"Telefone: {dados_empresa['telefone']}")],
            [sg.Text(f"CNPJ: {dados_empresa['cnpj']}")],
            [sg.Button("OK")],
        ]
        janela = sg.Window("Detalhes da Empresa", layout)
        janela.read()
        janela.close()

    def seleciona_empresa(self):
        layout = [
            [sg.Text("CNPJ da empresa que deseja selecionar:")],
            [sg.Input(key="cnpj")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]
        janela = sg.Window("Selecionar Empresa", layout)
        evento, valores = janela.read()
        janela.close()

        if evento == "Confirmar":
            return valores["cnpj"]
        return None

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem")

