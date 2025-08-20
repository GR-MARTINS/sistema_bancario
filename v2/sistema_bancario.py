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
            
        elif opcao == "q":
            break

        else:
            print("Operação inválida! Por favor, seleciona novamente a operação desejada.")
            

if __name__ == "__main__":
    main() 