import textwrap
from abc import ABC, abstractmethod
from datetime import date, datetime

class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: "Conta", transacao: "Transacao"):
        transacao.registrar(conta)

    def adicionar_conta(self, conta:"Conta"):
        self.contas.append(conta)
        
    def __repr__(self):
        atributos = []
        
        for chave, valor in self.__dict__.items():
            if isinstance(valor, list):
                atributos.append(f"{chave}=[...]")  # evita poluição
                
            else:
                atributos.append(f"{chave}={valor!r}")
                
        return f"{self.__class__.__name__}({', '.join(atributos)})"


class PessoaFisica(Cliente):
    def __init__(self, cpf:int, nome: str, endereco:str, data_nascimento: date):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.data_nascimento = data_nascimento


class Conta:
    def __init__(self, numero_da_conta: int, cliente: Cliente):
        self._saldo = 0
        self._numero = numero_da_conta
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, numero:int, cliente: Cliente):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
        
    def sacar(self, valor: int):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
    
        if excedeu_saldo:
            print("\nNão foi possível realizar o saque. Você não possui saldo suficiente")
            
        elif valor > 0:
            self._saldo -= valor
            print(f"\nSaque no valor de R$ {valor:.2f} realizado com sucesso!")
            return True
        
        else:
            print("\nNão foi possível realizar o saque. Valor inválido!")
            
        return False
    
    def depositar(self, valor: int):
        if valor > 0:
            self._saldo += valor
            print(f"\nDepósito no valor de R$ {valor:.2f} realizado com sucesso!")
        
        else:
            print("\nNão foi possível realizar o depósito. Valor inválido!")
            return False
        
        return True

    def __repr__(self):
        atributos = []
        
        for chave, valor in self.__dict__.items():
            if isinstance(valor, list):
                atributos.append(f"{chave}=[...]")  # evita poluição
                
            else:
                atributos.append(f"{chave}={valor!r}")
                
        return f"{self.__class__.__name__}({', '.join(atributos)})"
       
        
class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: Cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saque
        
    def sacar(self, valor: int):
        numero_saque = len(
            [
                transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__
            ]
        )
    
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saque >= self.limite_saques
        
        if excedeu_limite:
            print("\nNão foi possível realizar o saque. O valor do saque excede o limite da conta.")
            
        elif excedeu_saques:
            print("\nNão foi possível realizar o saque. Numero máximo de saques excedidos.")
    
        else:
            return super().sacar(valor)
        
        return False
       
        
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    @transacoes.setter
    def transacoes(self, transacao: "Transacao"):
        self._transacoes.append(transacao)
        
    def adicionar_transacao(self, transacao: "Transacao"):
        self.transacoes = {
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        }
        
    def __repr__(self):
        atributos = []
        
        for chave, valor in self.__dict__.items():
            if isinstance(valor, list):
                atributos.append(f"{chave}=[...]")  # evita poluição
                
            else:
                atributos.append(f"{chave}={valor!r}")
                
        return f"{self.__class__.__name__}({', '.join(atributos)})"
    
    
# interface = classe abstrata
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @classmethod
    @abstractmethod
    def registrar(cls, conta: Conta):
        pass
    
    
class Saque(Transacao):
    def __init__(self, valor: int):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta: Conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    
            
class Deposito(Transacao):
    def __init__(self, valor:int):
        self._valor = valor
    
    @property   
    def valor(self):
        return self._valor
    
    def registrar(self, conta: Conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)



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
            print(textwrap.dedent(f"\n{transacao["tipo"]} no valor de R$ {transacao["valor"]:.2f} realizado em {transacao["data"]}"))
            print("-------------------")
            
    else:
        print("Até o momento, não houve nenhuma movimentação na conta")
        
    print(f"\nSaldo: R$ {conta.saldo:.2f}")
    print("\n=========================================")


def criar_cliente(clientes: list[Cliente]):
    cpf = input("Digite o seu CPF (somente os números): ")
    
    try:
        cpf = int(cpf)
    except ValueError:
        
        print("Não foi possivel cadastrar o cliente. No campo CPF não foram informados somente números.")
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
        data_de_nascimento = datetime.strptime(data_de_nascimento,"%Y-%m-%d")
        
    except Exception:
        print("Não foi possivel cadastrar o cliente. Data de nascimento inválida.")
        return None
    
    cliente = PessoaFisica(cpf, nome, endereco, data_de_nascimento.date())
    print(f"\n{cliente.nome}, agora você é nosso cliente, boas vindas!\nAcesse como cliente e crie sua conta.")
    return cliente
    

def filtrar_cliente(cpf: int, clientes:list[PessoaFisica]):
    try:
        cpf = int(cpf)
        
    except ValueError:
        print("Cliente não localizado! CPF inválido")
        return None
    
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None


def criar_conta(contador_contas: int, cliente: Cliente):
    conta = ContaCorrente(contador_contas, cliente)
    
    if conta:
        cliente.adicionar_conta(conta)
        print(f"\n{cliente.nome}, sua conta foi criada com sucesso!")
        print(f"Agencia: {conta.agencia}\nNumero da conta: {conta.numero}")
        return conta


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
                        conta = criar_conta(contador_de_contas, cliente)
                        if conta:
                            contador_de_contas +=1
                            
                            
                    elif opcao == "lc":
                        listar_contas(cliente.contas)

                    elif opcao == "q":
                        break

                    else:
                        print("Operação inválida! Por favor, seleciona novamente a operação desejada.")

        if opcao_principal == "qs":
            cliente = criar_cliente(clientes)
            if cliente:
                clientes.append(cliente)
        
        if opcao_principal == "q":
            print("sessão encerrada!")
            break
            
if __name__ == "__main__":
    main()        