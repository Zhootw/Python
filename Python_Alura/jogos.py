import forca
import Adivinhacao

print("----------------------------------")
print("Escolha o seu jogo!!!")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual o jogo?"))



if (jogo == 1):
    print("jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("jogando adivinhação")
    Adivinhacao.jogar()