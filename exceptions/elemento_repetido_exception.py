class ElementoRepetidoException(Exception):
    def __init__(self, mensagem="Atenção! Esse elemento já existe"):
        super().__init__(mensagem)