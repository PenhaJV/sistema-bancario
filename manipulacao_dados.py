clientes = {
    "cliente1": 0  # Cliente: valor do saldo
}


def sacar():
    while True:
        try:
            saque = input("insira o valor: ").replace(",", ".")
            saque = float(saque)
            if not saque <= 0:
                if not clientes["cliente1"] < saque:
                    clientes["cliente1"] -= saque
                    print("Saque efetuado")
                    break
                else:
                    print("Saldo insuficiente")
                    break
            else:
                print("\nInsira um valor maior que zero.")

        except ValueError:
            print("\nInsira um valor válido")


def depositar():
    while True:
        try:
            deposito = input("insira o valor: ").replace(",", ".")
            deposito = float(deposito)
            if not deposito <= 0:
                clientes["cliente1"] += deposito
                print("Depósito efetuado")
                break
            else:
                print("\nInsira um valor maior que zero.")
        except ValueError:
            print("\nInsira um valor válido")


def extrato():
    for i in clientes.values():
        print(f"Saldo: R$ {i:.2f}")
        print()
