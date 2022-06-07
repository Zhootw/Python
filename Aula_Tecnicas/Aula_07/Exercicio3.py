#Faça um algoritmo que receba e calcule seu fatorial N!

#primeiro fazendo o calculo diminuindo os numero 5 4 3 2 1 e depois o calculo que é a multiplicacao
num = int(input("Insira um numero para calcular o seu fatorial: "))
cont = num
fatorial = 1
while cont > 0:
    print(cont)
    fatorial = fatorial * cont
    cont = cont -1

print(fatorial)




