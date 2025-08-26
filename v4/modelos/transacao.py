from __future__ import annotations
from abc import ABC, abstractmethod

# interface = classe abstrata
class Transacao(ABC):
    contador = 0

    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(cls, conta: "Conta"):
        pass


class Saque(Transacao):
    def __init__(self, valor: int):
        Saque.contador += 1
        self._id = Saque.contador
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @property
    def id(self):
        return self._id

    def registrar(self, conta: "Conta"):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor: int):
        Deposito.contador += 1
        self._id = Deposito.contador
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @property
    def id(self):
        return self._id

    def registrar(self, conta: "Conta"):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)