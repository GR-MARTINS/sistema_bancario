from __future__ import annotations
from datetime import datetime


class Historico:
    contador = 0

    def __init__(self):
        Historico.contador += 1
        self._id = Historico.contador
        self._transacoes = []

    @classmethod
    def from_dict(cls, dict: dict):
        obj = cls()
        obj.id = dict["id"]
        for item in dict["transacoes"]:
            obj.transacoes = item
        return obj

    def to_dict(self):
        dicionario = {"id": self.id, "transacoes": self.transacoes}
        return dicionario

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def transacoes(self):
        return self._transacoes

    @transacoes.setter
    def transacoes(self, transacao: dict):
        self._transacoes.append(transacao)

    def adicionar_transacao(self, transacao: "Transacao"):
        self.transacoes = {
            "id": transacao.id,
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        }

    def __repr__(self):
        atributos = []

        for chave, valor in self.__dict__.items():
            if isinstance(valor, list):
                atributos.append(f"{chave}=[...]")  # evita poluição

            else:
                atributos.append(f"{chave}={valor!r}")

        return f"{self.__class__.__name__}({', '.join(atributos)})"
