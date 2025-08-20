def menu():
    menu = """
    Selecione uma das opções abaixo:
    
     [d] Depositar
     [s] Sacar
     [e] Extrato
    [nu] Novo Usuário
    [lu] Listar Usuários
    [nc] Nova conta
    [lc] Listar Contas
     [q] Sair

    =>"""
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else: 
        print("Não foi possível realizar o depósito. Valor inválido!")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
        
    excedeu_limite = valor > limite
    
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("Não foi possível realizar o saque. Você não possui saldo suficiente")
        
    elif excedeu_limite:
        print("Não foi possível realizar o saque. O valor do saque excede o limite da conta.")
        
    elif excedeu_saques:
        print("Não foi possível realizar o saque. Numero máximo de saques excedidos.")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:     \t R$ {valor:.2f}\n"
        numero_saques += 1
    
    else:
        print("Não foi possível realizar o saque. O valor informado é invalido.")
        
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n=================EXTRATO=================")
    print("Até o momento, não houve nenhuma movimentação na conta" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n=========================================")


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    data_de_nascimento = input("Digite a data de nascimento do usuário: ")
    cpf = input("Digite o CPF do usuário (somente os números): ")
    endereco = input(
        "Digite o endereço do usuario (formato: logradouro, número - bairro - cidade/UF): "
        )
    
    try:
        cpf = int(cpf)
    except ValueError:
        print("Não foi possivel criar o usuário. No campo CPF não foram informados somente números.")
        return None
    
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Não foi possível criar o usuário. Já existe um usuário com esse CPF.")
        return None
    else:
        usuarios.append(
            {
                "nome": nome,    
                "data de nascimento": data_de_nascimento,
                "cpf": cpf,
                "endereço": endereco
            }
        )
        print(f"O usuário {nome} foi criado com sucesso!")
    return usuarios


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Digite o valor que você deseja depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)
                
        elif opcao == "s":
            valor = float(input("Digite o valor que você deseja sacar: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
                
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            usuarios = criar_usuario(usuarios)   

        elif opcao == "q":
            break

        else:
            print("Operação inválida! Por favor, seleciona novamente a operação desejada.")
            

if __name__ == "__main__":
    main() 