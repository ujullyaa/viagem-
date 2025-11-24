from daos.dao import DAO
from model.empresa_transporte import EmpresaTransporte
import re


class EmpresaTransporteDAO(DAO):
    def __init__(self):
        super().__init__('empresa_transporte.pkl')

    def __limpa_cnpj(self, cnpj: str) -> str:
        if not isinstance(cnpj, str):
            cnpj = str(cnpj)
        return re.sub(r'\D', '', cnpj)

    def __limpa_telefone(self, telefone: str) -> str:
        if not isinstance(telefone, str):
            telefone = str(telefone)
        return re.sub(r'\D', '', telefone)

    def add(self, empresa: EmpresaTransporte):
        if empresa is not None:
            empresa.cnpj = self.__limpa_cnpj(empresa.cnpj)
            empresa.telefone = self.__limpa_telefone(empresa.telefone)
            super().add(empresa.cnpj, empresa)

    def update(self, empresa: EmpresaTransporte):
        if empresa is not None:
            empresa.cnpj = self.__limpa_cnpj(empresa.cnpj)
            empresa.telefone = self.__limpa_telefone(empresa.telefone)
            super().update(empresa.cnpj, empresa)

    def get(self, cnpj: str):
        cnpj = self.__limpa_cnpj(cnpj)
        return super().get(cnpj)

    def remove(self, cnpj: str):
        cnpj = self.__limpa_cnpj(cnpj)
        super().remove(cnpj)

    def get_all(self):
        return list(super().get_all())
