nota = 0
total = 0
for n in range(1, 3):
    while ((nota < 0) and (nota > 10)):
        print("a nota deve ser de 0 a 10")
        nota = float(input("Insira a nota do aluno: "))
    total = total + nota
    resultado = total / 3

print(resultado)









