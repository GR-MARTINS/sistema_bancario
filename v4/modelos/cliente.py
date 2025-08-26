from __future__ import annotations
from datetime import datetime, date


class Cliente:

    contador = 0

    def __init__(self, endereco: str):
        Cliente.contador += 1
        self._id = Cliente.contador
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: "Conta", transacao: "Transacao"):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: "Conta"):
        self.contas.append(conta)

    def __repr__(self):
        atributos = []

        for chave, valor in self.__dict__.items():
            if isinstance(valor, list):
                atributos.append(f"{chave}=[...]")  # evita poluição

            else:
                atributos.append(f"{chave}={valor!r}")

        return f"{self.__class__.__name__}({', '.join(atributos)})"


class PessoaFisica(Cliente):
    def __init__(self, cpf: int, nome: str, endereco: str, data_nascimento: date):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.data_nascimento = data_nascimento

    @classmethod
    def from_dict(cls, pessoa_fisica: dict):
        obj = cls()
        obj.id = pessoa_fisica["id"]
        obj.cpf = pessoa_fisica["cpf"]
        obj.nome = pessoa_fisica["nome"]
        obj.endereco = pessoa_fisica["endereco"]
        obj.data_nascimento = datetime().strptime(
            pessoa_fisica["data_nascimento"], 
            "%Y-%m-%d").date()
        return obj
    
    def to_dict(self):
        dicionario = {
            "id": self.id,
            "cpf": self.cpf,
            "nome": self.nome,
            "endereco": self.endereco,
            "data_nascimento": self.data_nascimento
        }
        return dicionario