#Exercicio recursivo com fatorial
def somatorio(n):
    if n == 1:
        return 1
    else:
        return somatorio(n - 1) + n

print(somatorio(5))


# 5 + 4 + 3 + 2 + 1 = 15
    