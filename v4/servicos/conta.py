from modelos.cliente import Cliente
from modelos.conta import Conta, ContaCorrente


def criar_conta(cliente: Cliente):
    conta = ContaCorrente(cliente)

    if conta:
        cliente.adicionar_conta(conta)
        print(f"\n{cliente.nome}, sua conta foi criada com sucesso!")
        print(f"Agencia: {conta.agencia}\nNumero da conta: {conta.numero}")


def filtrar_conta(numero_conta: int, cliente: Cliente):
    try:
        numero_conta = int(numero_conta)

    except ValueError:
        return None

    for conta in cliente.contas:
        if conta.numero == numero_conta:
            return conta

    return None


def listar_contas(contas: list[Conta]):
    if contas != []:
        for conta in contas:
            print(
                f"""
                Agencia:\t{conta.agencia}
                Numero da conta:\t{conta.numero} 
                """
            )
