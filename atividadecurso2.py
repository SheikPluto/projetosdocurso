def calculadora(numero1, numero2, operacao):
    if operacao == 1:
        return numero1 + numero2
    elif operacao == 2:
        return numero1 - numero2
    elif operacao == 3:
        return numero1 * numero2
    elif operacao == 4 and numero2 != 0:
        return numero1 / numero2
    else:
        return 0

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
op = int(input("Escolha a operação (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))

resultado = calculadora(num1, num2, op)

print("Resultado:", resultado)