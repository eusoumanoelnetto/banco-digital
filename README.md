# Banco Digital - Projeto v1

## Descrição
Projeto simples de um sistema bancário utilizando Python. Nesta versão, temos:
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
