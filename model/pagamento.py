from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, forma_pagamento: str, pagou: bool, data: str, valor_total: float, passageiro):
        self.__forma_pagamento = forma_pagamento
        self.__pagou = pagou
        self.__data = data
        self.__valor_total = valor_total
        self.__passageiro = passageiro
        self.__codigo = None 

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def forma_pagamento(self):
        return self.__forma_pagamento

    @property
    def pagou(self):
        return self.__pagou

    @pagou.setter
    def pagou(self, status):
        self.__pagou = status

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, valor):
        self.__valor_total = valor

    @property
    def passageiro(self):
        return self.__passageiro

    @passageiro.setter
    def passageiro(self, passageiro):
        self.__passageiro = passageiro

    @abstractmethod
    def processar_pagamento(self) -> bool:
        pass

class Cedula(Pagamento):
    def __init__(self, forma_pagamento, pagou, data, valor_total, passageiro):
        super().__init__(forma_pagamento, pagou, data, valor_total, passageiro)

    def processar_pagamento(self) -> bool:
        return True

class Cartao(Pagamento):
    def __init__(self, forma_pagamento, pagou, data, valor_total, passageiro, numero_cartao, validade, bandeira, nome_titular):
        super().__init__(forma_pagamento, pagou, data, valor_total, passageiro)
        self.__numero_cartao = numero_cartao
        self.__validade = validade
        self.__bandeira = bandeira
        self.__nome_titular = nome_titular

    def processar_pagamento(self) -> bool:
        return True

class Pix(Pagamento):
    def __init__(self, forma_pagamento, pagou, data, valor_total, passageiro, chave_pix, banco):
        super().__init__(forma_pagamento, pagou, data, valor_total, passageiro)
        self.__chave_pix = chave_pix
        self.__banco = banco

    def processar_pagamento(self) -> bool:
        return True