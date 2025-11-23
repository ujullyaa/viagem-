import FreeSimpleGUI as sg

class TelaMeioTransporte:
    def __init__(self):
        sg.theme("DarkBlue3")
        self._tipos_fixos = ["Onibus", "Carro", "Avião"]

    def tela_opcoes(self):
        layout = [
            [sg.Column(
                [
                    [sg.Text("🚍 Menu Meio de Transporte", font=("Segoe UI", 18, "bold"))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("1 - Incluir Meio de Transporte", size=(35, 1))],
                    [sg.Button("2 - Alterar Meio de Transporte", size=(35, 1))],
                    [sg.Button("3 - Listar Meios de Transporte", size=(35, 1))],
                    [sg.Button("4 - Excluir Meio de Transporte", size=(35, 1))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("0 - Voltar ao Menu Principal", button_color=("white", "red"), size=(35, 1))]
                ],
                element_justification="center",
                expand_x=True
            )]
        ]
        window = sg.Window("Meios de Transporte", layout, element_justification="center")
        event, _ = window.read()
        window.close()

        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"): return 0
        if event == "1 - Incluir Meio de Transporte": return 1
        if event == "2 - Alterar Meio de Transporte": return 2
        if event == "3 - Listar Meios de Transporte": return 3
        if event == "4 - Excluir Meio de Transporte": return 4
        return 0

    def pega_dados_meio_transporte(self, meio=None):
        tipo = meio.tipo if meio else ""
        cap = meio.capacidade if meio else ""

        layout = [
            [sg.Text("🚍 Dados do Veículo", font=("Segoe UI", 14, "bold"))],
            [sg.Text("Tipo:", size=(15,1)), sg.Combo(self._tipos_fixos, default_value=tipo, size=(43,1), key="-TIPO-", readonly=True)],
            [sg.Text("Capacidade:", size=(15,1)), sg.Input(str(cap), size=(45,1), key="-CAP-")],
            [sg.HorizontalSeparator()],
            [sg.Button("💾 Confirmar", size=(20,1)), sg.Button("↩️ Cancelar", size=(20,1))]
        ]
        window = sg.Window("Cadastro Veículo", layout, element_justification="center")
        event, values = window.read()
        window.close()

        if event == "💾 Confirmar":
            return {"tipo": values["-TIPO-"], "capacidade": values["-CAP-"]}
        return None

    def seleciona_meio_transporte(self, meios):
        # Se a lista estiver vazia, o controlador avisa.
        # Aqui vamos usar TABELA para selecionar (muito melhor que combo)
        headers = ["Tipo", "Capacidade", "Empresa"]
        rows = []
        # Mapeamento para retornar o OBJETO correto, pois não temos ID simples aqui
        mapa_objetos = {} 
        
        for idx, m in enumerate(meios):
            emp_nome = m.empresa_transporte.nome_empresa if m.empresa_transporte else "N/A"
            rows.append([m.tipo, m.capacidade, emp_nome])
            mapa_objetos[idx] = m

        layout = [
            [sg.Text("Selecione o Veículo:", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, max_col_width=50, auto_size_columns=True,
                    justification='center', key="tabela", enable_events=True, select_mode='browse', 
                    expand_x=True, expand_y=True)],
            [sg.Button("Confirmar", size=(20,1)), sg.Button("Cancelar", size=(20,1))]
        ]

        window = sg.Window("Seleção", layout, size=(800, 400), element_justification="center")
        
        meio_selecionado = None
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"): break
            if event == "Confirmar":
                if values["tabela"]:
                    idx_tabela = values["tabela"][0]
                    meio_selecionado = mapa_objetos[idx_tabela]
                    break
                else:
                    sg.popup("Selecione uma linha!")
        
        window.close()
        return meio_selecionado

    def lista_meios(self, meios):
        # Reutiliza a lógica de tabela, mas sem retornar seleção
        if not meios:
            sg.popup("Nenhum meio cadastrado.")
            return
        
        headers = ["Tipo", "Capacidade", "Empresa"]
        rows = [[m.tipo, m.capacidade, (m.empresa_transporte.nome_empresa if m.empresa_transporte else "N/A")] for m in meios]

        layout = [
            [sg.Text("📋 Frota Cadastrada", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, max_col_width=50, auto_size_columns=True,
                    justification='center', expand_x=True, expand_y=True)],
            [sg.Button("Voltar", size=(20,1))]
        ]
        window = sg.Window("Lista", layout, size=(800, 400), element_justification="center")
        window.read()
        window.close()

    def seleciona_empresa(self, empresas):
        # Transforma em Tabela também para padronizar
        headers = ["Nome", "CNPJ"]
        rows = [[e.nome_empresa, e.cnpj] for e in empresas]
        mapa = {idx: e for idx, e in enumerate(empresas)}

        layout = [
            [sg.Text("Selecione a Empresa Proprietária:", font=("Segoe UI", 14))],
            [sg.Table(values=rows, headings=headers, auto_size_columns=True, key="tab", select_mode='browse', expand_x=True, expand_y=True)],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Seleção Empresa", layout, size=(600, 300))
        empresa_obj = None
        
        while True:
            ev, val = window.read()
            if ev in (sg.WINDOW_CLOSED, "Cancelar"): break
            if ev == "Confirmar":
                if val["tab"]:
                    empresa_obj = mapa[val["tab"][0]]
                    break
        window.close()
        return empresa_obj

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Aviso", font=("Segoe UI", 11))