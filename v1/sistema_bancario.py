menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite o valor que você deseja depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2}\n"

        else: 
            print("Não foi possível realizar o depósito. Valor inválido!")
            
    elif opcao == "s":
        valor = float(input("Digite o valor que você deseja sacar: "))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Não foi possível realizar o saque. Você não possui saldo suficiente")
            
        elif excedeu_limite:
            print("Não foi possível realizar o saque. O valor do saque excede o limite da conta.")
            
        elif excedeu_saques:
            print("Não foi possível realizar o saque. Numero máximo de saques excedidos.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2}"
            numero_saques += 1
        
        else:
            print("Não foi possível realizar o saque. O valor informado é invalido.")
            
    elif opcao == "q":
        break

    else:
        print("Operação inválida! Por favor, seleciona novamente a operação desejada.")
        