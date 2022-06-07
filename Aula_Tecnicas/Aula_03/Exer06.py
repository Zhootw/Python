print("Digite um ano para saber se ele é um ano Bissexto")

ano = int(input("Insira o ano:"))

if((ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0))):
    print("O ano ", ano, " é Bissexto!")

else:
    print("O ano ", ano, " Nao eh Bissexto!")