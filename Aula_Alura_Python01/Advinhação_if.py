print("******************************")
print("Bem Vindo ao jogo de adivinhacao!!!!!!")
print("******************************")

numero_secreto = 42


chute_str = input("Digite o seu numero: ")

print("voce digitou: ", chute_str)

chute = int(chute_str)

## meu jeito de fazer
##if(numero_secreto == chute):
##    print("Voce acertou")
##else:
##    if(numero_secreto >= chute):
##        print("o numero digitado é menor que o numero secreto!!")
##    else:
##        print("O numero digitado é maior que o numero secreto!!!!")
##   print("voce errou!")


acertou = chute == numero_secreto
maior = chute < numero_secreto
menor = chute > numero_secreto

if(acertou):
    print("Voce acertou")
else:
    if(maior):
        print("voce errou!")
        print("o numero digitado é menor que o numero secreto!!")
    elif(menor):
        print("voce errou!")
        print("O numero digitado é maior que o numero secreto!!!!")
    print("tente novamente!")


print("fim de jogo!!!!!")