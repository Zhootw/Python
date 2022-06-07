print("******************************")
print("Bem Vindo ao jogo de adivinhacao!!!!!!")
print("******************************")

numero_secreto = 42
tentativas = 5
rodada = 1

while(rodada <= tentativas):

    ## {} é string interpolation
    print("tentativas {} de {}".format(rodada, tentativas))
    chute_str = input("Digite o seu numero: ")

    print("voce digitou: ", chute_str)

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute < numero_secreto
    menor = chute > numero_secreto

    if(acertou):
        print("Voce acertou")
    else:
        if(maior):
            print("voce errou! O numero digitado é menor que o numero secreto!!!!")
        elif(menor):
            print("voce errou! O numero digitado é maior que o numero secreto!!!!")
            
    rodada = rodada + 1


    if(tentativas > 0):
        print("tente novamente!")

print("Sem tentativas restantes")
print("fim de jogo!!!!!")
























