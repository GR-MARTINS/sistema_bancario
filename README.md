# 💰 Sistema Bancário em Python

Este repositório contém a evolução de um projeto de sistema bancário, desenvolvido como parte dos desafios da [DIO](https://www.dio.me/) e posteriormente expandido.  
O objetivo é implementar operações bancárias em Python, introduzindo conceitos gradualmente:

- **v1** → implementação básica (sem funções e sem POO).  
- **v2** → modularização com funções + cadastro de usuários e contas.  
- **v3** → refatoração completa utilizando **Programação Orientada a Objetos (POO)**.  
- **v4** → persistência em arquivos JSON + modularização em pacotes.  
- **v5+** → futuras expansões (banco de dados, APIs, etc.).  

---

## 📌 Estrutura do Repositório

```
📁 sistema_bancario/
│── 📁 v1/   # Versão inicial (sem funções, sem POO)
│── 📁 v2/   # Versão com funções e cadastro de usuários/contas
│── 📁 v3/   # Versão com POO
│── 📁 v4/   # Versão com persistência em JSON e modularização em pacotes
│── README.md
```

Cada versão possui um **README.md próprio**, detalhando a implementação daquela etapa.

---

## 🚀 Evolução por Versão

- **v1**
  - Código sequencial, sem funções e sem POO.
  - Funcionalidades: depósito, saque (limite de R$500 e 3 saques/dia) e extrato.

- **v2**
  - Introdução de **funções** para modularizar o código.
  - Criação de **usuários** (nome, CPF, data de nascimento, endereço).
  - Criação e listagem de **contas bancárias** vinculadas a usuários.

- **v3**
  - Refatoração para **Programação Orientada a Objetos (POO)**.
  - Implementação de classes como `Cliente`, `PessoaFisica`, `Conta`, `ContaCorrente`, `Historico`, `Transacao`, `Saque` e `Deposito`.
  - Cada cliente gerencia suas próprias contas (não há mais listagem de todos os clientes).
  - Extrato agora é obtido a partir do histórico de transações, com registro de data/hora.
  - Baseado no **diagrama UML fornecido pela DIO**.

- **v4**
  - Introdução de **persistência em arquivos JSON** (`db.json`).
  - Modularização em pacotes:
    - `modelos/` → classes principais (`cliente`, `conta`, `historico`, `transacao`).
    - `servicos/` → regras de negócio (`cliente`, `conta`, `transacao`).
    - `utils/` → persistência (`armazenamento.py`) e menus.
  - Criação de `main.py` como **ponto de entrada** do sistema.
  - Prepara terreno para próximas funcionalidades: **PessoaJuridica, ContaPJ, ContaPoupança, senha para transações e acesso às contas**.

---

## 🛠 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- Estrutura modular com pacotes
- Persistência em **JSON**

---

## 👨‍💻 Sobre o Autor / Jornada

Este projeto foi desenvolvido como parte dos cursos **Python Fundamentals** e **Suzano - Python Developer #2**, realizado na [DIO](https://www.dio.me/) e ministrado pelo professor [**Guilherme Arthur de Carvalho**.  ](https://www.linkedin.com/in/decarvalhogui/)

Sou **supervisor administrativo** em transição de carreira para a área de **desenvolvimento web**.  
Tenho formação em **Matemática Industrial** e atualmente curso **Gestão de TI**.  

Já possuo experiência prática com:  
- **Python, Django, SQL, HTML, CSS, JavaScript**  
- Experimentos e estudos com frameworks de desenvolvimento web  
- Projetos práticos de bootcamps na área de desenvolvimento  

Minha motivação para realizar este curso foi **relembrar conceitos de Python, revisar boas práticas** e iniciar a construção do meu **portfólio de desenvolvedor**.  
Aprendi Python de forma **autodidata** e agora estou organizando meus projetos aqui no GitHub como parte da minha evolução profissional.  

---

## ✨ Autor

Implementado por [*Glayton Martins*](https://www.linkedin.com/in/gr-martins/).
