# 💰 Sistema Bancário em Python - Versão 1 (v1)

Esta é a **primeira versão (v1)** do sistema bancário, desenvolvida em Python.  
Até o momento, **não foram utilizadas funções nem Programação Orientada a Objetos (POO)**.  

O código foi escrito de forma sequencial para atender aos requisitos básicos do desafio.

---

## 📌 Funcionalidades Implementadas

- **Depósito**
  - Aceita apenas valores positivos.
  - Movimentações registradas no extrato.

- **Saque**
  - Máximo de 3 saques diários.
  - Cada saque limitado a R$ 500,00.
  - Apenas permitido caso haja saldo disponível.
  - Movimentações registradas no extrato.

- **Extrato**
  - Lista todos os depósitos e saques realizados.
  - Exibe o saldo atual.
  - Caso não haja movimentações, exibe:  
    `Até o momento, não houve nenhuma movimentação na conta`.

---

## 📂 Estrutura da Versão v1

```
📁 v1/
│── sistema_bancario.py   # Código principal da versão 1
│── README.md             # Documentação da versão 1
```

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. No terminal, navegue até a pasta `v1` e execute:

```bash
python sistema_bancario.py
```

3. Use o menu interativo para operar o sistema.

---

## 📖 Exemplo de Uso

```
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Digite o valor que você deseja depositar: 1000

=> s
Digite o valor que você deseja sacar: 200

=> e

=================EXTRATO=================
Depósito: R$ 1000.00
Saque:    R$ 200.00

Saldo: R$ 800.00
=========================================
```

---

## ✨ Observação

- Esta versão é **a base inicial** do projeto.  
- A evolução do código acontecerá em:
  - **v2** → introdução de funções.  
  - **v3** → refatoração em POO.  
