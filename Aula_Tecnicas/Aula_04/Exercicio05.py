def ispar(num = int):
    if(num % 2 == 0):
        return True
    else:
        return False

print("Insira um numero para ver se eh par ou impar:")
num = int(input("Digite o numero: "))

resultado = ispar(num)

par = resultado == True
impar = resultado == False
if(par):
    print("O numero escolhido eh Par!")
else:
    print("O numero escolhido eh impar!")

print(ispar(num))