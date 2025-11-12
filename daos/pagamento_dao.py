from daos.dao import DAO
from model.pagamento import Pagamento

# Implementação DAO para Pagamento
class PagamentoDAO(DAO):
    def __init__(self):
        super().__init__('pagamento.pkl')

    def add(self, pagamento: Pagamento):
        if((pagamento is not None) and isinstance(pagamento, Pagamento) and isinstance(pagamento.data, str)):
            super().add(pagamento.data, pagamento)

    def update(self, pagamento: Pagamento):
        if((pagamento is not None) and isinstance(pagamento, Pagamento) and isinstance(pagamento.data, str)):
            super().update(pagamento.data, pagamento)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if(isinstance(key, str)):
            return super().remove(key)
