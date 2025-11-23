class ElementoNaoExisteException(Exception):
    def __init__(self, mensagem="Atenção! Esse elemento não existe"):
        super().__init__(mensagem)