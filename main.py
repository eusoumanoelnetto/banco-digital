from app.conta import ContaBancaria

def menu():
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver extrato")
    print("4 - Sair")

def main():
    conta = ContaBancaria()
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                valor = float(input("Informe o valor do depósito: "))
                conta.depositar(valor)
            except ValueError:
                print("Valor inválido. Digite um número.")
        elif opcao == '2':
            try:
                valor = float(input("Informe o valor do saque: "))
                conta.sacar(valor)
            except ValueError:
                print("Valor inválido. Digite um número.")
        elif opcao == '3':
            conta.extrato()
        elif opcao == '4':
            print("Encerrando a sessão. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente!")

if __name__ == "__main__":
    main()
