from datetime import datetime
from modelos.cliente import Cliente, PessoaFisica


def criar_cliente(clientes: list[Cliente]):
    cpf = input("Digite o seu CPF (somente os números): ")

    try:
        cpf = int(cpf)
    except ValueError:

        print(
            "Não foi possivel cadastrar o cliente. No campo CPF não foram informados somente números."
        )
        return None

    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Não foi cadastrar o cliente. Já existe um cliente com esse CPF.")
        return None

    nome = input("Digite seu nome: ")

    endereco = input(
        "Digite o endereço seu endereço (formato: logradouro, número - bairro - cidade/UF): "
    )

    data_de_nascimento = input("Digite a data de nascimento do cliente (ano-mes-dia): ")

    try:
        data_de_nascimento = datetime.strptime(data_de_nascimento, "%Y-%m-%d")

    except Exception:
        print("Não foi possivel cadastrar o cliente. Data de nascimento inválida.")
        return None

    cliente = PessoaFisica(cpf, nome, endereco, data_de_nascimento.date())
    print(
        f"\n{cliente.nome}, agora você é nosso cliente, boas vindas!\nAcesse como cliente e crie sua conta."
    )
    return cliente


def filtrar_cliente(cpf: int, clientes: list[PessoaFisica]):
    try:
        cpf = int(cpf)

    except ValueError:
        print("Cliente não localizado! CPF inválido")
        return None

    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None
