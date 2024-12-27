#solicitar 2 numeros como entrada e depois vamos realizar uma operação de soma, subtração, multiplicação e divisão
info1 = float(input("Digite o primeiro numero: "))
info2 = float(input("Digite o segundo numero: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")
if operacao == '+':
    print("A soma dos numeros é: ", info1 + info2)
elif operacao == '-':
    print("A subtração dos numeros é: ", info1 - info2)
elif operacao == '*':
    print("A multiplicação dos numeros é: ", info1 * info2)
elif operacao == '/':
    print("A divisão dos numeros é: ", info1 / info2)
else:
    print("Operação inválida")
# O que acontece se o usuario digitar um texto?
# O que acontece se o usuario digitar um numero decimal?
# O que acontece se o usuario digitar um numero negativo?
# O que acontece se o usuario digitar um texto que pode ser convertido para inteiro?

