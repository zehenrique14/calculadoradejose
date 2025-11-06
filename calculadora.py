#calculadora simples
# fonte: https://www.reddit.com/r/learnpython/comments/1k0ettl/creating_a_simple_calculator_with_python/?tl=pt-br
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Operações")
print("1:adição")
print("2:subtração")
print("3:multiplicação")
print("4:divisão")

operacao = input("Escolha uma operação: ")

if (operacao == "1"):
    resultado = num1 + num2
    print(resultado)
elif (operacao == "2"):
    resultado = num1 - num2
    print(resultado)
elif (operacao == "3"):
    resultado = num1 * num2
    print(resultado)
elif (operacao == "4"):
    resultado = num1 / num2
    if (num2 != 0):
        print(resultado)
    else: 
        print("erro: número é zero")
else:
    print("números inválidos")
    # calculadora