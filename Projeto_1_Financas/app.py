receitas = []
despesas = []

while True:
    print("\n1 - Adicionar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Ver Saldo")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        valor = float(input("Valor da receita: "))
        receitas.append(valor)

    elif opcao == "2":
        valor = float(input("Valor da despesa: "))
        despesas.append(valor)

    elif opcao == "3":
        saldo = sum(receitas) - sum(despesas)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "4":
        break