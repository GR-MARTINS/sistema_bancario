# 💰 Sistema Bancário em Python - Versão 2 (v2)

A versão **v2** do sistema bancário traz a modularização do código, com uso de **funções** para organizar as operações, além da introdução de **usuários e contas bancárias**.  

---

## 📌 Funcionalidades Implementadas

- **Depósito (`depositar`)**
  - Argumentos somente por posição (positional only).
  - Aceita apenas valores positivos.
  - Retorna saldo e extrato.

- **Saque (`sacar`)**
  - Argumentos somente por nome (keyword only).
  - Respeita limite de saldo, limite por saque (R$ 500) e até 3 saques por dia.
  - Retorna saldo e extrato.

- **Extrato (`exibir_extrato`)**
  - Argumentos mistos (saldo posicional e extrato nomeado).
  - Lista todas as movimentações.
  - Exibe saldo atual.

- **Usuários**
  - Criar usuário (`criar_usuario`) → armazena nome, data de nascimento, CPF e endereço.
  - Lista de usuários.
  - Não permite CPFs duplicados.

- **Contas**
  - Criar conta (`criar_conta`) → agência fixa "0001", número da conta sequencial, vinculação ao usuário via CPF.
  - Um usuário pode ter mais de uma conta.
  - Listar contas cadastradas.

---

## 📂 Estrutura da Versão v2

```
📁 v2/
│── sistema_bancario.py   # Código principal da versão 2
│── README.md             # Documentação da versão 2
```

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. No terminal, navegue até a pasta `v2` e execute:

```bash
python sistema_bancario.py
```

3. Utilize o menu interativo para realizar as operações:

```
 [d] Depositar
 [s] Sacar
 [e] Extrato
[nu] Novo Usuário
[lu] Listar Usuários
[nc] Nova Conta
[lc] Listar Contas
 [q] Sair
```

---

## 📖 Exemplo de Uso

```
=> nu
Digite o nome do usuário: João Silva
Digite a data de nascimento do usuário: 01/01/1990
Digite o CPF do usuário (somente os números): 12345678900
Digite o endereço do usuario (formato: logradouro, número - bairro - cidade/UF): Rua A, 10 - Centro - São Paulo/SP

=> nc
Digite o CPF do usuário (somente os números): 12345678900
Sua conta foi criada com sucesso!

=> d
Digite o valor que você deseja depositar: 500
Depósito realizado com sucesso!

=> e

=================EXTRATO=================
Depósito:    R$ 500.00

Saldo: R$ 500.00
=========================================
```

---

## ✨ Observação

- Esta versão introduz a modularização do código e a criação de usuários e contas.
- A evolução do projeto continuará em:
  - **v3** → refatoração em Programação Orientada a Objetos (POO).  
