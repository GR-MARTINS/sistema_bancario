from servicos.cliente import filtrar_cliente, criar_cliente
from servicos.conta import criar_conta, listar_contas
from servicos.transacao import depositar, exibir_extrato, sacar
from utils.menus import menu_pessoal, menu_principal

def main():

    clientes = []
    contador_de_contas = 1
    sair = False

    while not sair:

        opcao_principal = menu_principal()

        if opcao_principal == "sc":
            cpf = input("Digite seu cpf para continuar: ")

            cliente = filtrar_cliente(cpf, clientes)

            print(f"\nOlá {cliente.nome}, em que posso te ajudar hoje?")
            if cliente:
                while True:

                    opcao = menu_pessoal()

                    if opcao == "d":
                        depositar(cliente)

                    elif opcao == "s":
                        sacar(cliente)

                    elif opcao == "e":
                        numero_da_conta = input("Digite o número da conta: ")
                        exibir_extrato(numero_da_conta, cliente)

                    elif opcao == "nc":
                        conta = criar_conta(cliente)
                        if conta:
                            contador_de_contas += 1

                    elif opcao == "lc":
                        listar_contas(cliente.contas)

                    elif opcao == "q":
                        break

                    else:
                        print(
                            "Operação inválida! Por favor, seleciona novamente a operação desejada."
                        )

        if opcao_principal == "qs":
            cliente = criar_cliente(clientes)
            if cliente:
                clientes.append(cliente)

        if opcao_principal == "q":
            print("sessão encerrada!")
            break


if __name__ == "__main__":
    main()
