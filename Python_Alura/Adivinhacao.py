import random

def jogar():

    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print("Bem vindo no jogo da advinhação!")

    numero_secreto = round(random.randrange(1, 101))
    tentativas = 0
    pontos = 1000

    #print(numero_secreto)

    print("Qual o nivel de dificuldade? ")
    print("(1) Fácil, (2) Médio, (3) Difícil")

    nivel = int(input("Defina o Nível: "))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5


    for rodada in range(1, tentativas + 1):
        print("Quantidades de tentativas: ", rodada ," de ", tentativas)
        chute = int(input("Digite um numero de 1 a 100: "))
        print("voce digitou ", chute)

        if((chute < 1) or (chute > 100)):
            print("O valor digitado precisa ser de 1 a 100!")
            continue

        acertou = chute == numero_secreto
        menor   = chute < numero_secreto
        maior   = chute > numero_secreto

        if (acertou):
            print("Acertou !!!")
            print("Voce fez ", pontos, " Pontos!!")
            break
        else:
            if(menor):
                print("O valor digitado é menor que o numero secreto, errou!!")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
                
            else:#maior
                print("O valor digitado é maior que o numero secreto, errou!!")


    print("Fim de jogo!!")