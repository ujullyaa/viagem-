import FreeSimpleGUI as sg

class TelaEmpresaTransporte:

    def tela_opcoes(self):
        layout = [
            [sg.Column(
                [
                    [sg.Text("🏢 Menu Empresa de Transporte", font=("Segoe UI", 18, "bold"))],
                    [sg.HorizontalSeparator()],
                    [sg.Button("1 - Incluir Empresa", size=(35, 1))],
                    [sg.Button("2 - Alterar Empresa", size=(35, 1))],
                    [sg.Button("3 - Listar Empresas", size=(35, 1))],
                    [sg.Button("4 - Excluir Empresa", size=(35, 1))],
                    [sg.Button("0 - Voltar ao Menu Principal", button_color=("white", "red"), size=(35, 1))]
                ],
                element_justification="center",
                expand_x=True
            )]
        ]

        window = sg.Window(
            "Menu Empresa",
            layout,
            element_justification="center"
        )

        event, values = window.read()
        window.close()

        if event in (sg.WINDOW_CLOSED, "0 - Voltar ao Menu Principal"):
            return 0
        elif event == "1 - Incluir Empresa":
            return 1
        elif event == "2 - Alterar Empresa":
            return 2
        elif event == "3 - Listar Empresas":
            return 3
        elif event == "4 - Excluir Empresa":
            return 4
        return -1


    def pega_dados_empresa(self, empresa=None):
        nome_default = empresa.nome_empresa if empresa else ""
        cnpj_default = empresa.cnpj if empresa else ""
        telefone_default = empresa.telefone if empresa else ""

        layout = [
            [sg.Text("🏢 Cadastro de Empresa", font=("Segoe UI", 18, "bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Nome da Empresa:", size=(18, 1)), 
            sg.Input(default_text=nome_default, key="nome", size=(45, 1))],

            [sg.Text("CNPJ:", size=(18, 1)), 
            sg.Input(default_text=cnpj_default, key="cnpj", disabled=empresa is not None, size=(45, 1))],

            [sg.Text("Telefone:", size=(18, 1)), 
            sg.Input(default_text=telefone_default, key="telefone", size=(45, 1))],

            [sg.HorizontalSeparator()],
            [sg.Button("💾 Confirmar", key="confirmar", size=(18, 1)),
            sg.Button("↩️ Cancelar", key="cancelar", size=(18, 1))]
        ]

        window = sg.Window(
            "Cadastro/Alteração de Empresa",
            layout,
            element_justification="center",
            finalize=True
        )

        event, values = window.read()
        window.close()

        if values is None or event in (sg.WINDOW_CLOSED, "cancelar"):
            return None

        if event == "confirmar":
            return {
                "nome": values.get("nome", "").strip(),
                "cnpj": values.get("cnpj", "").strip(),
                "telefone": values.get("telefone", "").strip()
            }
        return None


    def mostra_empresas(self, empresas):
        if isinstance(empresas, list):
            if not empresas:
                sg.popup("Nenhuma empresa encontrada.", title="📋 Lista de Empresas")
                return None

            headers = ["CNPJ", "Nome", "Telefone"]
            rows = [[empresa.cnpj, empresa.nome_empresa, empresa.telefone] for empresa in empresas]

            layout = [
                [sg.Text("📋 Lista de Empresas", font=("Segoe UI", 14, "bold"))],
                [sg.HorizontalSeparator()],

                [sg.Table(values=rows, headings=headers, max_col_width=50,
                        auto_size_columns=True, expand_x=True, expand_y=True,
                        key="tabela_empresas", enable_events=True, select_mode='browse',
                        justification="center")],

                [sg.Button("Confirmar", size=(20, 1)),
                sg.Button("Cancelar", size=(20, 1))]
            ]

            window = sg.Window(
                "Lista de Empresas",
                layout,
                size=(650, 400),  # tabela mais larga
                element_justification="center",
                finalize=True
            )

            while True:
                event, values = window.read()

                if event in (sg.WINDOW_CLOSED, "Cancelar"):
                    window.close()
                    return None

                if event == "Confirmar":
                    selected = values.get("tabela_empresas")
                    if selected:
                        idx = selected[0]
                        cnpj = rows[idx][0]
                        window.close()
                        return cnpj
                    else:
                        sg.popup("Selecione uma empresa antes de confirmar.")
        else:
            sg.popup_scrolled(
                f"CNPJ: {empresas.cnpj}\nNome: {empresas.nome}",
                title="📋 Empresa",
                font=("Segoe UI", 11)
            )


    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem")
