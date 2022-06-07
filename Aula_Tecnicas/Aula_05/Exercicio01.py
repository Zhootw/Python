def e_multiplo(n1: int, n2: int) -> bool:
    return n1 % n2 == 0

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if(e_multiplo(n1, n2)):
    print(f'{n1} é multiplo de {n2}.')

else:
    print(f'{n1} nao eh multiplo de {n2}.')