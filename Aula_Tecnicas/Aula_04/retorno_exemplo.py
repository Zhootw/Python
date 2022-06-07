# dica de entrada e de retorno
def somar(n1 : int, n2 : int) ->int:
    resultado = n1 + n2
    return resultado


n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))


print(somar(n1, n2))

#ou

resposta = somar(n1, n2)
print("o valor do calculo eh: ", resposta)