#Um número inteiro maior que 1 é primo se ele possui como divisores
#apenas 1 e ele mesmo. Faça um algoritmo que leia um número e
#verifique se é primo.


num = int(input("Insira o numero para verificar se el eh um numero primo: "))

primo = num / num == 1
primo2 = num % 2 == 0
primo3 = num % 3 == 0

if(primo and primo2):
    print("O numero eh primo!")
else:
    print("o numero nao eh primo!")









