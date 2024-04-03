menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            continue

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            continue

        if valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
            continue

        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
            continue

        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimentacao in extrato:
                print(movimentacao)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")