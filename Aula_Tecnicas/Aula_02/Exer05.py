import datetime
print("calculadora de idade:")

nascimento = int(input("Digite o ano de seu nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

calculo = ano_atual - nascimento

print("a sua idade atual eh: ", calculo, " anos")