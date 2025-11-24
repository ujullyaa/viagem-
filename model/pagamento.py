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
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def forma_pagamento(self):
        return self.__forma_pagamento

    @property
    def pagou(self):
        return self.__pagou

    @pagou.setter
    def pagou(self, pagou: bool):
        self.__pagou = pagou

    @property
    def data(self):
        return self.__data

    @property
    def valor_total(self):
        return self.__valor_total

    @property
    def passageiro(self):
        return self.__passageiro

    @abstractmethod
    def processar_pagamento(self):
        pass
class Cartao(Pagamento):
    def __init__(self, forma_pagamento: str, pagou: bool, data: str, valor_total: float, passageiro,
                 numero_cartao: str, validade: str, bandeira: str, titular: str):
        super().__init__(forma_pagamento, pagou, data, valor_total, passageiro)
        self.__numero_cartao = numero_cartao
        self.__validade = validade
        self.__bandeira = bandeira
        self.__titular = titular

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @property
    def validade(self):
        return self.__validade

    @property
    def bandeira(self):
        return self.__bandeira

    @property
    def titular(self):
        return self.__titular

    def processar_pagamento(self):
        if self.pagou:
            print(f"💳 Pagamento no cartão ({self.bandeira}) confirmado para {self.titular}.")
        else:
            print("❌ Pagamento no cartão não concluído.")
class Pix(Pagamento):
    def __init__(self, forma_pagamento: str, pagou: bool, data: str, valor_total: float, passageiro,
                chave_pix: str, banco: str):
        super().__init__(forma_pagamento, pagou, data, valor_total, passageiro)
        self.__chave_pix = chave_pix
        self.__banco = banco

    @property
    def chave_pix(self):
        return self.__chave_pix

    @property
    def banco(self):
        return self.__banco

    def processar_pagamento(self):
        if self.pagou:
            print(f"⚡ Pagamento via PIX ({self.banco}) realizado com sucesso.")
        else:
            print("❌ Pagamento via PIX não realizado.")

class Cedula(Pagamento):
    def __init__(self, forma_pagamento: str, pagou: bool, data: str, valor_total: float, passageiro):
        super().__init__(forma_pagamento, pagou, data, valor_total, passageiro)

    def processar_pagamento(self):
        if self.pagou:
            print(f"💵 Pagamento em dinheiro no valor de R$ {self.valor_total:.2f} confirmado.")
        else:
            print("❌ Pagamento em dinheiro pendente.")
