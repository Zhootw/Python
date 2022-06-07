from email.mime import base


def area_triangulo(altura = int, base = int):
    area = altura * base
    return area

print("Digite a altura e base para calcular a area de um triangulo:")
altura = int(input("Digite a altura: "))
base = int(input("Digite a base: "))

resultado = area_triangulo(altura, base)

print("a area do triangulo eh : ", resultado)