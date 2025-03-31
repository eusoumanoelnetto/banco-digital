class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.deposito_hist = []  # Histórico dos depósitos
        self.saque_hist = []     # Histórico dos saques
        self.num_saques = 0      # Quantidade de saques realizados hoje

    def depositar(self, valor):
        if valor <= 0:
            print("Ops! O valor deve ser positivo.")
            return
        self.saldo += valor
        self.deposito_hist.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if valor <= 0:
            print("Ops! O valor deve ser positivo.")
            return
        if valor > 500:
            print("Limite máximo por saque é de R$ 500,00.")
            return
        if self.num_saques >= 3:
            print("Você já realizou 3 saques hoje.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque!")
            return

        self.saldo -= valor
        self.saque_hist.append(valor)
        self.num_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def extrato(self):
        print("\n--- Extrato ---")
        print("Depósitos:")
        if self.deposito_hist:
            for i, valor in enumerate(self.deposito_hist, start=1):
                print(f"  Depósito {i}: R$ {valor:.2f}")
        else:
            print("  Nenhum depósito realizado.")

        print("\nSaques:")
        if self.saque_hist:
            for i, valor in enumerate(self.saque_hist, start=1):
                print(f"  Saque {i}: R$ {valor:.2f}")
        else:
            print("  Nenhum saque realizado.")

        print(f"\nSaldo atual: R$ {self.saldo:.2f}\n")
