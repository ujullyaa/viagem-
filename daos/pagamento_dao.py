from daos.dao import DAO
from model.pagamento import Pagamento

class PagamentoDAO(DAO):
    def __init__(self):
        super().__init__('pagamento.pkl')

    def add(self, pagamento: Pagamento):
        if pagamento is not None:
            super().add(pagamento.codigo, pagamento)

    def update(self, pagamento: Pagamento):
        if pagamento is not None:
            super().update(pagamento.codigo, pagamento)

    def get(self, codigo: str):
        return super().get(codigo)

    def remove(self, codigo: str):
        super().remove(codigo)

    def get_all(self):
        return list(super().get_all())
