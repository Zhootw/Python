
def jogar():

    print("=============================================")
    print("Bem vindo no jogo da forca!")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_",]

    enforcou = False
    acertou = False

    #enquanto nao acertar ou nao errar
    #enquanto (TRUE and TRUE)
    while(not enforcou and not acertou):

        chute = input("Qual letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

            print(letras_acertadas)

        print("jogando ....")

    print("Fim de jogo!!")


if(__name__ == "__main__"):
    jogar()
