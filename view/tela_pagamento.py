import FreeSimpleGUI as sg

class TelaPagamento:
    def __init__(self):
        pass

    def tela_opcoes(self):
        layout = [
            [sg.Text("Menu Pagamento", font=("Helvetica", 15))],
            [sg.Button("Cadastrar Pagamento", key=1)],
            [sg.Button("Listar Pagamentos", key=2)],
            [sg.Button("Excluir Pagamento", key=3)],
            [sg.Button("Voltar", key=0)]
        ]

        window = sg.Window("Menu Pagamento", layout)
        event, _ = window.read()
        window.close()

        if event in (sg.WINDOW_CLOSED, 0):
            return 0
        elif event == 1:
            return 1
        elif event == 2:
            return 2
        elif event == 3:
            return 3
        return 0

    def pega_dados_pagamento(self):
        layout = [
            [sg.Text("Código do Pagamento:"), sg.Input(key="codigo")],
            [sg.Text("Forma de Pagamento:"), sg.Combo(["Cartão", "Dinheiro", "Pix"], key="forma", readonly=True)],
            [sg.Text("Valor (R$):"), sg.Input(key="valor")],
            [sg.Text("Status:"), sg.Combo(["Pendente", "Concluído"], key="status", readonly=True)],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Pagamento", layout)
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return {
                "codigo": values["codigo"],
                "forma": values["forma"],
                "valor": values["valor"],
                "status": values["status"]
            }
        return None

    def mostra_pagamento(self, dados):
        sg.popup(
            f"Código: {dados['codigo']}\n"
            f"Forma: {dados['forma']}\n"
            f"Valor: R$ {dados['valor']}\n"
            f"Status: {dados['status']}",
            title="Pagamento"
        )

    def mostra_pagamentos(self, pagamentos):
        if not pagamentos:
            sg.popup("Nenhum pagamento cadastrado.")
            return
        texto = ""
        for p in pagamentos:
            texto += (
                f"Código: {p['codigo']}\n"
                f"Forma: {p['forma']}\n"
                f"Valor: R$ {p['valor']}\n"
                f"Status: {p['status']}\n\n"
            )
        sg.popup_scrolled(texto, title="Pagamentos Cadastrados")

    def seleciona_pagamento(self):
        layout = [
            [sg.Text("Digite o código do pagamento:")],
            [sg.Input(key="codigo")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Pagamento", layout)
        event, values = window.read()
        window.close()

        if event == "Confirmar":
            return values["codigo"]
        return None

    def mostra_mensagem(self, msg):
        sg.popup(msg)
