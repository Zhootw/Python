print("******************************")
print("Bem Vindo ao jogo de adivinhacao!!!!!!")
print("******************************")

numero_secreto = 42
erro = 1
tentativas = 5

##while(erro == 1):
while(tentativas != 0):
    chute_str = input("Digite o seu numero: ")

    print("voce digitou: ", chute_str)

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute < numero_secreto
    menor = chute > numero_secreto

    if(acertou):
        print("Voce acertou")
        ##erro = 2
    else:
        if(maior):
            print("voce errou! ainda tem :", tentativas - 1, ("tentativas disponiveis"))
            print("o numero digitado é menor que o numero secreto!!")
            ##erro = 1
            tentativas = tentativas - 1
        elif(menor):
            print("voce errou! ainda tem :", tentativas - 1, ("tentativas disponiveis"))
            print("O numero digitado é maior que o numero secreto!!!!")
            ##erro = 1
            tentativas = tentativas - 1
    if(tentativas > 0):
        print("tente novamente!")

print("Sem tentativas restantes")
print("fim de jogo!!!!!")