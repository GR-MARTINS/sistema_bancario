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

    else:
        print("Operação inválida! Por favor, seleciona novamente a operação desejada.")
        