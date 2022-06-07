#Crie uma função que calcule a soma dos termos de uma progressão aritmética.
termo = int(input("insira o termo: "))

razao = int(input("Insira a razao: "))

qtd_termos = int(input("Insira a quantidade de termos: "))

cont = termo
cont1 = termo

while cont <= qtd_termos:
    cont1 = cont1 + razao
    print(f'{cont1} ', end='')
    cont = cont +1

print("Agora com For....")
resultado = termo

for n in range(1, qtd_termos):
    resultado = resultado + razao
    print(f'{resultado} ', end='')
    #print(razao)




