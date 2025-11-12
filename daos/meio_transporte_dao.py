from daos.dao import DAO
from model.meio_transporte import MeioTransporte

class MeioTransporteDAO(DAO):
    def __init__(self):
        super().__init__('meio_transporte.pkl')

    def add(self, meio: MeioTransporte):
        if meio is not None:
            super().add(meio.codigo, meio)

    def update(self, meio: MeioTransporte):
        if meio is not None:
            super().update(meio.codigo, meio)

    def get(self, codigo: str):
        return super().get(codigo)

    def remove(self, codigo: str):
        super().remove(codigo)

    def get_all(self):
        return list(super().get_all())
