def calcular_media(nota1: float, nota2: float, nota3: float) -> float:
    media = (nota1 + nota2 + nota3) / 3
    return media

n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segundo nota: "))
n3 = int(input("Digite a terceiro nota: "))


media = calcular_media(n1, n2, n3)

print("A média das tres notas eh: ", media)