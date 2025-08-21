# 💰 Sistema Bancário em Python - Versão 3 (v3)

A versão **v3** do sistema bancário marca a refatoração completa do projeto utilizando **Programação Orientada a Objetos (POO)**.  
Foi a etapa final do desafio da **DIO**, baseada no diagrama UML fornecido.

---

## 📌 Funcionalidades Implementadas

- **Clientes**
  - Classe `Cliente` e `PessoaFisica`.
  - Cada cliente pode possuir múltiplas contas.
  - Métodos para realizar transações e gerenciar contas.

- **Contas**
  - Classe `Conta` (genérica) e `ContaCorrente` (especializada).
  - Agência fixa: `0001`.
  - Limite de saque: R$ 500,00.
  - Limite de 3 saques por dia.

- **Transações**
  - Interface `Transacao` (classe abstrata).
  - Implementações: `Saque` e `Deposito`.
  - Histórico de transações registrado com valor, tipo e data/hora.

- **Histórico**
  - Cada conta possui um `Historico` com todas as transações.
  - Extrato exibe a lista formatada de movimentações.

- **Menus**
  - Menu principal: acessar como cliente ou cadastrar novo cliente.
  - Menu pessoal: depósito, saque, extrato, criação e listagem de contas.

---

## 📂 Estrutura da Versão v3

```
📁 v3/
│── sistema_bancario.py   # Código principal da versão 3 (POO)
│── UML.png               # Diagrama UML fornecido pela DIO
│── README.md             # Documentação da versão 3
```

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. No terminal, navegue até a pasta `v3` e execute:

```bash
python sistema_bancario.py
```

3. Utilize os menus para realizar as operações.

---

## 📖 Exemplo de Uso

```
=> qs
Digite o seu CPF (somente os números): 12345678900
Digite seu nome: João Silva
Digite o endereço seu endereço (formato: logradouro, número - bairro - cidade/UF): Rua A, 10 - Centro - São Paulo/SP
Digite a data de nascimento do cliente (ano-mes-dia): 1990-01-01

João Silva, agora você é nosso cliente, boas vindas!
Acesse como cliente e crie sua conta.

=> sc
Digite seu cpf para continuar: 12345678900
Olá João Silva, em que posso te ajudar hoje?

=> nc
João Silva, sua conta foi criada com sucesso!
Agencia: 0001
Numero da conta: 1

=> d
Digite o número da conta: 1
Informe o valor do depósito: 1000
Depósito no valor de R$ 1000.00 realizado com sucesso!

=> e
=================EXTRATO=================

Deposito no valor de R$ 1000.00 realizado em 19-08-2025 17:35:00
-------------------

Saldo: R$ 1000.00
=========================================
```

---

## ✨ Observação

- Esta versão encerra a parte oficial do desafio da DIO.  
- Próximas versões (v4, v5, v6...) serão expansões próprias:  
  - **v4** → manipulação de arquivos (persistência em JSON, login com senha).  
  - **v5** → banco de dados.  
  - **v6** → API.  
