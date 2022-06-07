print("Digite a sua idade para saber qual categoria:")

idade = int(input("Insira a sua idade: "))

##basic
if(idade < 5):
    print("Sua idade eh: ", idade, " sendo assim sua categoria eh: Bebe")
elif(idade >= 5 and idade <= 7):
    print("Sua idade eh: ", idade, " sendo assim sua categoria eh: Infantil A")
elif(idade >= 8 and idade <= 10):
    print("Sua idade eh: ", idade, " sendo assim sua categoria eh: infantil B")
elif(idade >= 11 and idade <= 13):
    print("Sua idade eh: ", idade, " sendo assim a sua categoria eh: Juvenil A")
elif(idade >= 14 and idade <= 17):
    print("Sua idade eh: ", idade, " sendo assim a sua categoria eh: juvenil B")
else:
    print("Sua idade eh: ", idade, " sendo assim sua categoria eh senior")

##advanced
print("Advanced!!!!!!!!!")

Bebe = (idade < 5)
Infantil_A = (idade >= 5 and idade <= 7)
Infantil_B = (idade >= 8 and idade <= 10)
Juvenil_A = (idade >= 11 and idade <= 13)
Juvenil_B = (idade >= 14 and idade <= 17)
Senior = (idade >= 18)

if(Bebe):
    print("Sua idade eh: ", idade, " sendo assim sua categoria eh: Bebe")
elif(Infantil_A):
    print("Sua idade eh: ", idade, " sendo assim sua categoria eh: Infantil A")
elif(Infantil_B):
    print("Sua idade eh: ", idade, " sendo assim sua categoria eh: infantil B")
elif(Juvenil_A):
    print("Sua idade eh: ", idade, " sendo assim a sua categoria eh: Juvenil A")
elif(Juvenil_B):
    print("Sua idade eh: ", idade, " sendo assim a sua categoria eh: juvenil B")
elif(Senior):
    print("Sua idade eh: ", idade, " sendo assim sua categoria eh senior")



