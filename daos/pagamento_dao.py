from daos.dao import DAO
from model.pagamento import Pagamento


class PagamentoDAO(DAO):
    def __init__(self):
        super().__init__('pagamento.pkl')

    def add(self, pagamento: Pagamento):
        if pagamento and isinstance(pagamento, Pagamento) and isinstance(pagamento.codigo, int):
            super().add(str(pagamento.codigo), pagamento)

    def update(self, pagamento: Pagamento):
        if pagamento and isinstance(pagamento, Pagamento) and isinstance(pagamento.codigo, int):
            super().update(str(pagamento.codigo), pagamento)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(str(key))

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(str(key))
