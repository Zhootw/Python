def media_nota(nota1: float, nota2: float, nota3: float, nota4: float) -> float:
    soma = nota1 + nota2 + nota3 + nota4
    menor = min(nota1, nota2, nota3, nota4)
    calculo = soma - menor

    media = calculo / 3

    return media

nota1 = float(input("Digita a primeira nota: "))
nota2 = float(input("Digita a segunda nota: "))
nota3 = float(input("Digita a terceira nota: "))
nota4 = float(input("Digita a quarta nota: "))

resposta = media_nota(nota1, nota2, nota3, nota4)

print("a media eh: ", resposta)