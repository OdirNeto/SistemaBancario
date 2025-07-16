# Bootcamp Santander – Backend with Python: Sistema Bancário (CLI)

> **PT-BR:** Este projeto é um sistema bancário simples em linha de comando, desenvolvido como parte do **Bootcamp Santander – Backend with Python**. Ele permite operações básicas como depósito, saque, extrato, cadastro de usuários e criação/listagem de contas. Os dados são mantidos **somente em memória** durante a execução (não há persistência em arquivo ou banco de dados).
>
> **EN:** This is a simple command-line banking system built for the **Santander Backend with Python Bootcamp**. It supports deposits, withdrawals, account statements, user registration, and account creation/listing. All data lives **in memory only** (no persistence between runs).

---

## 🧭 Sumário / Table of Contents

* [Sobre o Projeto / About](#-sobre-o-projeto--about)
* [Recursos / Features](#-recursos--features)
* [Regras de Negócio / Business Rules](#-regras-de-negócio--business-rules)
* [Pré-requisitos / Requirements](#-pré-requisitos--requirements)
* [Como Rodar / How to Run](#-como-rodar--how-to-run)
* [Demonstração no Terminal / Terminal Demo](#-demonstração-no-terminal--terminal-demo)
* [Estrutura do Código / Code Structure](#-estrutura-do-código--code-structure)
* [Próximos Passos / Next Steps](#-próximos-passos--next-steps)
* [Contribuindo / Contributing](#-contribuindo--contributing)
* [Licença / License](#-licença--license)
* [Créditos / Credits](#-créditos--credits)

---

## 📌 Sobre o Projeto / About

Este projeto implementa um **mini-sistema bancário didático** para praticar conceitos de Python (funções, parâmetros posicionais vs nomeados, estruturas de dados, loops, entrada de usuário) durante o bootcamp. É executado totalmente no terminal e usa apenas a biblioteca padrão (`textwrap`).

This project implements a **learning-focused mini banking system** to practice Python concepts (functions, positional-only and keyword-only params, data structures, loops, user input) in a bootcamp context. Runs entirely in the terminal and uses only the standard library (`textwrap`).

---

## 💡 Recursos / Features

**Português**

* Menu interativo no terminal.
* Depósito com validação de valor.
* Saque com limite por transação.
* Controle de número máximo de saques (por sessão – *ver nota em limitações*).
* Emissão de extrato com histórico de transações e saldo.
* Cadastro de usuários (nome, CPF, data de nascimento, endereço).
* Criação de contas vinculadas a usuários (agência fixa `0001`).
* Listagem de contas existentes.
* Mensagens amigáveis ao usuário.

**English**

* Interactive terminal menu.
* Deposit operation with basic validation.
* Withdrawal limited by per-transaction cap.
* Max withdrawals per session (see limitation note).
* Printable account statement (transactions + balance).
* User registration (name, CPF id, birth date, address).
* Account creation linked to existing users (fixed branch `0001`).
* List all created accounts.
* Friendly user-facing messages.

---

## ⚙ Regras de Negócio / Business Rules

| Regra                        | Valor / Comportamento | Observações                                                              |
| ---------------------------- | --------------------- | ------------------------------------------------------------------------ |
| Agência padrão               | `0001`                | Todas as novas contas usam esta agência.                                 |
| Limite de saque por operação | R\$ 500,00            | Verificado antes de processar.                                           |
| Número máximo de saques      | 3 (por sessão)        | Contador reseta quando o programa reinicia |
| Depósito mínimo              | R\$ 1,00              | Valores menores são recusados.                                           |
| Saque mínimo                 | R\$ 1,00              | Valores menores são recusados.                                           |
| Persistência de dados        | **Nenhuma**           | Tudo é perdido ao sair do programa.                                      |

---

## 🖥 Pré-requisitos / Requirements

* **Python 3.13** (ou compatível; foi desenvolvido/testado mirando 3.13).
* Sistema operacional com terminal (Windows, macOS, Linux).
* Nenhuma dependência externa além da **biblioteca padrão**.

---

## ▶ Como Rodar / How to Run

> Supondo que o arquivo principal se chame `main.py` (renomeie se necessário).

**Clonar o repositório / Clone repo**

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <PASTA_DO_PROJETO>
```

**Executar / Run**

```bash
python main.py   # macOS/Linux (ou python3)
# ou no Windows
py main.py
```

Se preferir rodar diretamente copiando o código sem Git, salve o conteúdo em `main.py` e execute conforme acima.

---

## 🖼 Demonstração no Terminal / Terminal Demo

A seguir um exemplo **simulado** de sessão no terminal (semelhante à saída real). Você pode substituir por um print real depois.

```text
======menu=====

[1] Extrato
[2] Depositar
[3] Sacar
[4] Criar Conta
[5] Listar Contas
[6] Cadastrar Novo Usuário
[0] Sair

===============

Por favor digite o numero da opção desejada: 6
Informe o numero do seu CPF (sem pontos ou caracteres especiais): 12345678900
Informe o seu nome completo: Maria Silva
Informe sua data de nascimento no seguinte formato: (dd-mm-aaaa): 01-01-1990
Informe seu endereço (logradouro, numero - bairro - cidade/sigla estado): Rua A, 100 - Centro - Fortaleza/CE

Usuário cadastrado com sucesso!
Seja bem vindo, Maria Silva

======menu=====
... escolha: 4
Informe o CPF do usuário: 12345678900
=== Sua conta foi criada com sucesso ===
=== Você já pode aproveitar as vantagens que só o nosso banco oferece para você ===

======menu=====
... escolha: 2
Informe o valor do deposito: R$200
A quantia de R$200.00 foi depositada com sucesso. Seu saldo atual é de R$200.00.

======menu=====
... escolha: 3
Informe o valor do saque: R$50
Saque realizado com sucesso. Seu saldo atual é de R$150.00

======menu=====
... escolha: 1
------------------------EXTRATO------------------------
Deposito: R$ 200.00
Saque: R$ 50.00

Seu saldo atual é de R$150.00
---------------------------------------------------------
```

## 🗂 Estrutura do Código / Code Structure

Projeto de arquivo único (pode evoluir depois para módulos separados):

```
.
├── main.py  # Código principal do sistema bancário (este arquivo)
└── README.md
```

### Principais Funções

| Função                                                                                  | Tipo de Parâmetros           | Responsabilidade                                                                           |
| --------------------------------------------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------ |
| `menu()`                                                                                | entrada do usuário           | Exibe opções e retorna escolha.                                                            |
| `extrato_da_conta(saldo, *, extrato)`                                                   | posicional + nomeado         | Mostra histórico e saldo.                                                                  |
| `depositar(saldo, valor, extrato, /)`                                                   | posicionais-only             | Valida e adiciona depósito; retorna novo saldo + extrato.                                  |
| `sacar(*, saldo, valor, extrato, limite_de_valor, saques_realizados, limite_de_saques)` | nomeados-only                | Valida regras de saque; retorna novo saldo + extrato.                                      |
| `criar_usuario(usuarios)`                                                               | lista mutável                | Coleta dados e adiciona usuário.                                                           |
| `filtrar_usuario(cpf, usuarios)`                                                        | utilitária                   | Busca usuário por CPF.                                                                     |
| `criar_conta(agencia, numero_conta, usuarios)`                                          | depende de usuário existente | Cria e retorna dicionário conta.                                                           |
| `listar_contas(contas)`                                                                 | leitura                      | Imprime contas existentes.                                                                 |
| `main()`                                                                                | orquestrador                 | Loop principal do sistema.                                                                 |

---

## 🤝 Contribuindo / Contributing

Quer sugerir melhorias? Faça um *fork* e abra um *pull request*.

**Fluxo sugerido**

```bash
git fork # (via GitHub UI)
git clone <SEU_FORK_URL>
cd <PASTA_DO_PROJETO>
git checkout -b feature/nome-da-feature
# edite, commit, push
# abra Pull Request
```

Ao contribuir, inclua breve descrição, por que a mudança é necessária e, se possível, passos para testar.

---

## 📄 Licença / License

**Nenhuma licença definida no momento.** Isso significa que, por padrão, todos os direitos são reservados. Se quiser permitir uso aberto, recomendo adicionar uma licença (por exemplo: MIT). Me avise se quiser que eu gere o arquivo `LICENSE` e atualize esta seção.

**No license selected yet.** By default, all rights reserved. Let me know if you want to add an open-source license (MIT recommended for learning projects), and I’ll update this section.

---

## 🙌 Créditos / Credits

Projeto desenvolvido por **Odir Neto** como parte do **Bootcamp Santander – Backend with Python**.

Se este projeto te ajudou, deixe uma ⭐ no repositório!

---

### Contato / Contact

* E-mail profissional: neto.odir@gmail.com

---
