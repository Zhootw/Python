import string


def validador_texto(texto: string) -> bool:

    if((len(texto) > 1) and (len(texto) <= 100)):
        return True

    else:
        return False

texto = input("Insira um texto para ver se esta entre 1 a 100 caracteres: ")

saida = validador_texto(texto)

print(saida)

if(saida == True):
    print("o texto digitado esta entre 1 e 100 caracteres")

else:
    print("o texto digitado nao esta entre 1 e 100 caracteresaa")