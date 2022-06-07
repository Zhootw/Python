def encontrar_max(num1 = int, num2 = int):
    if(num1 > num2):
        maior = num1
    else:
        maior = num2
    
    return maior
print("Digite 2 numeros para ver qual eh o maior")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))


resultado = encontrar_max(num1, num2)

print("O maior numero eh: ", resultado)
