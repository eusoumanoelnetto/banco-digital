# Sistema Bancário com Python

## Descrição

Este projeto é um sistema bancário simples desenvolvido em Python, que permite realizar operações básicas como depósitos, saques e consulta de extrato. O objetivo é demonstrar conceitos fundamentais de programação e estrutura de dados em Python, proporcionando uma base para iniciantes explorarem e expandirem suas habilidades na linguagem.

- **Depósito:** Permite depósitos de valores positivos, que são registrados em uma lista.
- **Saque:** Permite até 3 saques diários, com limite de R$ 500,00 por saque e verificação de saldo.
- **Extrato:** Lista todos os depósitos e saques realizados e exibe o saldo atual da conta, com formatação no padrão R$ xxx.xx.

## Estrutura do Projeto
```plaintext
banco-digital/
│── app/
│   ├── __init__.py
│   ├── conta.py
│── main.py
│── README.md
