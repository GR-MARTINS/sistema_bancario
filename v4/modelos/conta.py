from __future__ import annotations
from modelos.historico import Historico
from modelos.transacao import Saque


class Conta:
    contador = 0

    def __init__(self, cliente: "Cliente"):
        Conta.contador += 1
        self._id = Conta.contador
        self._saldo = 0
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente: "Cliente"):
        return cls(cliente)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def numero(self):
        return self._id

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @historico.setter
    def historico(self, historico):
        self._historico = historico

    def sacar(self, valor: int):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print(
                "\nNão foi possível realizar o saque. Você não possui saldo suficiente"
            )

        elif valor > 0:
            self._saldo -= valor
            print(f"\nSaque no valor de R$ {valor:.2f} realizado com sucesso!")
            return True

        else:
            print("\nNão foi possível realizar o saque. Valor inválido!")

        return False

    def depositar(self, valor: int):
        if valor > 0:
            self._saldo += valor
            print(f"\nDepósito no valor de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("\nNão foi possível realizar o depósito. Valor inválido!")
            return False

        return True

    def __repr__(self):
        atributos = []

        for chave, valor in self.__dict__.items():
            if isinstance(valor, list):
                atributos.append(f"{chave}=[...]")  # evita poluição

            else:
                atributos.append(f"{chave}={valor!r}")

        return f"{self.__class__.__name__}({', '.join(atributos)})"


class ContaCorrente(Conta):
    def __init__(self, cliente: "Cliente", limite=500, limite_saque=3):
        super().__init__(cliente)
        self.limite = limite
        self.limite_saques = limite_saque

    @classmethod
    def from_dict(cls, dict_conta: dict, cliente, dict_historico: dict):
        obj = cls(cliente)
        obj.id = dict_conta["id"]
        obj.saldo = dict_conta["saldo"]
        obj.agencia = dict_conta["agencia"]
        obj.historico = Historico.from_dict(dict_historico)
        return obj

    def to_dict(self):
        dicionario = {
            "id": self.id,
            "saldo": self.saldo,
            "agencia": self.agencia,
            "cliente_cpf": self.cliente.cpf,
            "historico_id": self.historico.id,
        }
        return dicionario

    def sacar(self, valor: int):
        numero_saque = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saque >= self.limite_saques

        if excedeu_limite:
            print(
                "\nNão foi possível realizar o saque. O valor do saque excede o limite da conta."
            )

        elif excedeu_saques:
            print(
                "\nNão foi possível realizar o saque. Numero máximo de saques excedidos."
            )

        else:
            return super().sacar(valor)

        return False
