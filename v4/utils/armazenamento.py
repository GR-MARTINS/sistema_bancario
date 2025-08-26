import json
from modelos.cliente import PessoaFisica, Cliente
from modelos.conta import ContaCorrente, Conta
from modelos.historico import Historico
from modelos.transacao import Transacao
from servicos.cliente import filtrar_cliente


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


def filtrar_historico(historico: dict, id: int):
    for item in historico:
        if item["id"] == id:
            return item


def carregar_contas(db: dict, clientes: list[Cliente]):
    print("Carregando contas ...")
    for conta in db["contacorrente"]:
        cliente = filtrar_cliente(conta["cliente_cpf"], clientes)
        historico = filtrar_historico(
            db["historico"]["historico"], conta["historico_id"]
        )
        cliente.contas.append(ContaCorrente.from_dict(conta, cliente, historico))


def inicializar_contadores(dict: dict):
    try:
        Cliente.contador = dict["cliente"]["contador"]
        Conta.contador = dict["conta"]["contador"]
        Historico.contador = dict["historico"]["contador"]
        Transacao.contador = dict["transacao_atual"]
    except:
        pass
