def menu_principal():
    menu = """
    Digite uma das opções abaixo para continuar:
    
    [sc] Sou Cliente
    [qs] Quero ser cliente
     [q] Sair
    
    => """
    return input(menu)


def menu_pessoal():
    menu = """
    Digite uma das opções abaixo para continuar:
    
     [d] Depositar
     [s] Sacar
     [e] Extrato
    [lc] Listar Contas
    [nc] Nova conta
     [q] Sair

    =>"""
    return input(menu)