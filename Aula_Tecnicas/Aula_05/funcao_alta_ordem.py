def adicao(num1: float , num2: float) -> float:
    return num1 + num2

def subtraicao(num1: float , num2: float) -> float:
    return num1 - num2

def calcular(num1: float , num2: float, operacao) -> float:
    resultado = operacao(num1, num2)
    return resultado

resultado = calcular(5, 2, adicao)
print(resultado)