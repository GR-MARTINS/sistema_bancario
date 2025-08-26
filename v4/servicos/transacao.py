import textwrap
from modelos.cliente import Cliente
from servicos.conta import filtrar_conta
from modelos.transacao import Deposito, Saque


def depositar(cliente: Cliente):
    numero_conta = input("Digite o número da conta: ")
    conta = filtrar_conta(numero_conta, cliente)

    if not conta:
        print("Depósito não realizado! Conta não encontrada!")
        return

    valor = input("Informe o valor do depósito: ")

    try:
        valor = int(valor)

    except ValueError:
        print("Depósito não realizado! Valor inválido.")
        return

    cliente.realizar_transacao(conta, Deposito(valor))


def sacar(cliente: Cliente):
    numero_conta = input("Digite o número da conta: ")
    conta = filtrar_conta(numero_conta, cliente)

    if not conta:
        print("Saque não realizado! Conta não encontrada!")
        return

    valor = input("Informe o valor do saque: ")

    try:
        valor = int(valor)

    except ValueError:
        print("Saque não realizado! Valor inválido.")
        return

    cliente.realizar_transacao(conta, Saque(valor))


def exibir_extrato(numero_da_conta: int, cliente: Cliente):
    conta = filtrar_conta(numero_da_conta, cliente)
    transacoes = conta.historico.transacoes

    print("\n=================EXTRATO=================")

    if transacoes != []:
        for transacao in transacoes:
            print(
                textwrap.dedent(
                    f"\n{transacao["tipo"]} no valor de R$ {transacao["valor"]:.2f} realizado em {transacao["data"]}"
                )
            )
            print("-------------------")

    else:
        print("Até o momento, não houve nenhuma movimentação na conta")

    print(f"\nSaldo: R$ {conta.saldo:.2f}")
    print("\n=========================================")
