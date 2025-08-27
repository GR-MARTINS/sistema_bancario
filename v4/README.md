# 💰 Sistema Bancário em Python - Versão 4 (v4)

A versão **v4** do sistema bancário marca a introdução da **persistência de dados em JSON** e a **reestruturação completa em pacotes**, preparando o sistema para novas expansões.  

---

## 📌 Funcionalidades Implementadas

- **Persistência de dados**
  - Dados de clientes, contas e transações armazenados em `db.json`.
  - Permite que as informações sejam mantidas mesmo após encerrar o programa.

- **Organização modular**
  - `modelos/` → classes principais (`cliente`, `conta`, `historico`, `transacao`).  
  - `servicos/` → regras de negócio (`cliente`, `conta`, `transacao`).  
  - `utils/` → persistência (`armazenamento.py`) e menus.  

- **Arquivo principal**
  - `main.py` → ponto de entrada do sistema.

- **Conceitos aplicados**
  - Modularização do código.  
  - Persistência em **arquivos JSON**.  
  - Separação de responsabilidades (*Single Responsibility Principle*).  

---

## 📂 Estrutura da Versão v4

```
📁 v4/
│── main.py
│── db.json
│── modelos/
│   │── cliente.py
│   │── conta.py
│   │── historico.py
│   │── transacao.py
│── servicos/
│   │── cliente.py
│   │── conta.py
│   │── transacao.py
│── utils/
│   │── armazenamento.py
│   │── menus.py
│── README.md
```

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. No terminal, navegue até a pasta `v4` e execute:

```bash
python main.py
```

3. Utilize os menus para criar clientes, contas e realizar transações.

---

## 📖 Próximos Passos (planejados)

- Implementar **PessoaJuridica** e `ContaPJ`.  
- Criar `ContaPoupanca`.  
- Adicionar **senha para transações** e **senha de acesso às contas**.  

---

## ✨ Observação

- Esta versão consolida a prática em **manipulação de arquivos** e **organização modular**.  
- Serve como ponte para as próximas versões, que trarão autenticação, novas contas e integração com banco de dados.  
