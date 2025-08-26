import json
from modelos.cliente import PessoaFisica


def carregar_dados():
    try:
        with open("db.json", "r") as f:
            db = json.load(f)
            return db

    except FileNotFoundError:
        return None


def carregar_clientes(db: dict):
    print("\nPor favor, aguarde!")
    print("Carregando clientes ...")

    clientes = []

    for cliente in db["pessoafisica"]:
        clientes.append(PessoaFisica.from_dict(cliente))
    return clientes
