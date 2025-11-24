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
                    [sg.Button("0 - Retornar", button_color=("white", "red"), size=(35, 1))]
                ],
                element_justification="center",
                expand_x=True
            )]
        ]
        
        window = sg.Window("Meios de Transporte", layout, element_justification="center")

        resultado = window.read()
        window.close()
        
        if resultado is None: 
            return 0
            
        event, _ = resultado

        if event in (sg.WINDOW_CLOSED, "0 - Retornar"): return 0
        
        opcoes = {
            "1 - Incluir Meio de Transporte": 1, 
            "2 - Alterar Meio de Transporte": 2, 
            "3 - Listar Meios de Transporte": 3, 
            "4 - Excluir Meio de Transporte": 4
        }
        return opcoes.get(event, 0)

    def pega_dados_meio_transporte(self, meio=None):

        tipo = meio.tipo if meio else ""
        cap = meio.capacidade if meio else ""

        layout = [
            [sg.Text("🚍 Dados do Veículo", font=("Segoe UI", 14, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Tipo:", size=(15,1)), sg.Combo(self._tipos_fixos, default_value=tipo, size=(43,1), key="-TIPO-", readonly=True)],
            [sg.Text("Capacidade:", size=(15,1)), sg.Input(str(cap), size=(45,1), key="-CAP-")],
            [sg.HorizontalSeparator()],
            [sg.Button("💾 Confirmar", size=(20,1)), sg.Button("↩️ Cancelar", size=(20,1))]
        ]
        window = sg.Window("Cadastro Veículo", layout, element_justification="center")
        
        resultado = window.read()
        window.close()

        if resultado is None: return None
        event, values = resultado

        if event == "💾 Confirmar":
            return {"tipo": values["-TIPO-"], "capacidade": values["-CAP-"]}
        return None

    def seleciona_meio_transporte(self, meios):
        if not meios:
            sg.popup("Nenhum meio cadastrado.", title="Aviso")
            return None

        headers = ["Tipo", "Capacidade", "Empresa"]
        rows = []
        mapa_objetos = {} 
        
        for idx, m in enumerate(meios):
            
            emp_nome = m.empresa_transporte.nome_empresa if hasattr(m, 'empresa_transporte') and m.empresa_transporte else "N/A"
            
            rows.append([m.tipo, m.capacidade, emp_nome])
            mapa_objetos[idx] = m 

        layout = [
            [sg.Text("Selecione o Veículo:", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, 
                    max_col_width=50, 
                    auto_size_columns=True,
                    justification='center', 
                    key="tabela", 
                    enable_events=True, 
                    select_mode='browse', 
                    expand_x=True, 
                    expand_y=True)],
            [sg.Button("Confirmar", size=(20,1)), sg.Button("Cancelar", size=(20,1))]
        ]

        window = sg.Window("Seleção", layout, size=(800, 400), element_justification="center")
        
        meio_selecionado = None
        while True:
            resultado = window.read()
            if resultado is None: break
            
            event, values = resultado
            
            if event in (sg.WINDOW_CLOSED, "Cancelar"): 
                break
            
            if event == "Confirmar":
                if values["tabela"]:
                    idx_tabela = values["tabela"][0]
                    
                    meio_selecionado = mapa_objetos[idx_tabela]
                    break
                else:
                    sg.popup("Selecione uma linha!", title="Aviso")
        
        window.close()
        return meio_selecionado

    def lista_meios(self, meios):
        if not meios:
            sg.popup("Nenhum meio cadastrado.", title="Aviso")
            return
        
        headers = ["Tipo", "Capacidade", "Empresa"]
        rows = []
        for m in meios:
            emp_nome = m.empresa_transporte.nome_empresa if hasattr(m, 'empresa_transporte') and m.empresa_transporte else "N/A"
            rows.append([m.tipo, m.capacidade, emp_nome])

        layout = [
            [sg.Text("📋 Frota Cadastrada", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, 
                    max_col_width=50, 
                    auto_size_columns=True,
                    justification='center', 
                    expand_x=True, 
                    expand_y=True)],
            [sg.Button("Voltar", size=(20,1))]
        ]
        window = sg.Window("Lista", layout, size=(800, 400), element_justification="center")
        
        
        window.read()
        window.close()

    def seleciona_empresa(self, empresas):
        headers = ["Nome", "CNPJ"]
        rows = [[e.nome_empresa, e.cnpj] for e in empresas]
        mapa = {idx: e for idx, e in enumerate(empresas)}

        layout = [
            [sg.Text("Selecione a Empresa Proprietária:", font=("Segoe UI", 14, "bold"))],
            [sg.Table(values=rows, headings=headers, 
                    auto_size_columns=True, 
                    justification='center', 
                    key="tab", 
                    select_mode='browse', 
                    expand_x=True, 
                    expand_y=True)],
            [sg.Button("Confirmar", size=(20,1)), sg.Button("Cancelar", size=(20,1))]
        ]
        
        window = sg.Window("Seleção Empresa", layout, size=(700, 400), element_justification="center")
        empresa_obj = None
        
        while True:
            resultado = window.read()
            if resultado is None: break
            
            ev, val = resultado
            
            if ev in (sg.WINDOW_CLOSED, "Cancelar"): break
            
            if ev == "Confirmar":
                if val["tab"]:
                    empresa_obj = mapa[val["tab"][0]]
                    break
                else:
                    sg.popup("Selecione uma empresa.", title="Aviso")
        window.close()
        return empresa_obj

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Aviso", font=("Segoe UI", 11))