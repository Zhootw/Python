print("digite 2 numeros para saber qual o maior ou se sao iguais")
num1 = int(input("digite o primeiro numero:"))
num2 = int(input("digite o segundo numero:"))

if(num1 > num2):
    print("o primeiro numero eh maior!")
elif(num2 > num1):
    print("o segundo numero eh maior!")
else:
    print("os numeros sao iguais!")

##ou podemos fazer facilitando mais o organizacao

maior = num1 > num2
menor = num1 < num2
#igual = num1 == num2

if(maior):
    print("o primeiro numero eh maior!!!!!")
elif(menor):
    print("o segundo numero eh maior!!!!!")
else:
    print("os numeros sao iguais!")

