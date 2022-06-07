n_letras = 0

for letra in "Primeiro meio ultimo":
    if letra == " ":
        break
    n_letras += 1 #quando o break for executado ele nao fara isso

print("O total de letras antes do primeiro espaco eh: ", n_letras)