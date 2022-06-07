#Faça um algoritmo que leia 30 valores e 
# conte quantos estão no intervalo [10,20], escrevendo ao final essa informação.


#cont = 0
#for n in range(0, 30):
#    n = n + 1
#    num = int(input(f'Insira o {n} numero de 30: '))
#    if((num >= 10) and (num <= 20)):
#        cont = cont + 1
#print(f'O resultado foi {cont}, numeros entre 10 e 20.')


cont1 = 0
cont2 = 0
while cont1 <= 29:
    cont1 = cont1 + 1
    num = int(input(f'Insira o {cont1} numero de 30: '))
    if((num >= 10) and (num <= 20)):
    	cont2 = cont2 + 1
    


print(f'O resultado foi {cont2}, numeros entre 10 e 20.')















