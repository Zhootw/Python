print("Calculadora, Digite 2 numeros e a operaçao desejada")

num1 = int(input("insira o primeiro numero: "))

num2 = int(input("insira o segundo numero: "))
print("Operadores: +, -, *, /")
operacao = input("insira a operacao desejada:")

if(operacao == "+"):
    calculo = num1 + num2
elif(operacao == "-"):
    calculo = num1 - num2
elif(operacao == "*"):
    calculo = num1 * num2
elif(operacao == "/"):
    calculo = num1 / num2
print("O calculo foi feito: ", num1, operacao, num2, " sendo o resultado: ", calculo)


        


