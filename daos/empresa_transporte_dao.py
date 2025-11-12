from daos.dao import DAO
from model.empresa_transporte import EmpresaTransporte

# Implementação DAO para EmpresaTransporte
class EmpresaTransporteDAO(DAO):
    def __init__(self):
        super().__init__('empresa_transporte.pkl')

    def add(self, empresa: EmpresaTransporte):
        if((empresa is not None) and isinstance(empresa, EmpresaTransporte) and isinstance(empresa.cnpj, int)):
            super().add(empresa.cnpj, empresa)

    def update(self, empresa: EmpresaTransporte):
        if((empresa is not None) and isinstance(empresa, EmpresaTransporte) and isinstance(empresa.cnpj, int)):
            super().update(empresa.cnpj, empresa)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if(isinstance(key, int)):
            return super().remove(key)
