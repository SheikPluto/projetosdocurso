def calculadora():
    while True:
        print("Escolha a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        escolha = int(input("Digite o número para a operação correspondente: "))

        if escolha == 0:
            print("Saindo da calculadora.")
            break
        elif escolha not in [1, 2, 3, 4]:
            print("Essa opção não existe. Tente novamente.")
            continue

        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))

        if escolha == 1:
            resultado = num1 + num2
            print("Resultado: ", resultado)
        elif escolha == 2:
            resultado = num1 - num2
            print("Resultado: ", resultado)
        elif escolha == 3:
            resultado = num1 * num2
            print("Resultado: ", resultado)
        elif escolha == 4:
            if num2 == 0:
                print("Divisão por zero não é permitida.")
            else:
                resultado = num1 / num2
                print("Resultado: ", resultado)

# Para rodar a calculadora, basta chamar a função:
calculadora()
