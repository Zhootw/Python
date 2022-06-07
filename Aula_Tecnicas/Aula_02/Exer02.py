print("Bem vindo, digite 4 numero que faremos uma soma do total")

##sempre bom lembrar de colocar o int pois ele reconhece como default string
num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))
num3 = int(input("Digite o terceiro numero:"))
num4 = int(input("Digite o quarto numero:"))

soma = num1 + num2 + num3 + num4
print("O resultado eh:", soma)


##melhorando (Avançado)

rodadas = 1
resposta = 0
while rodadas <= 4:
    print(rodadas ," numero de 4")
    numero = int(input("Digite o numero: "))
    resposta = resposta + numero
    rodadas = rodadas + 1

print("O resultado das soma eh: ", resposta)