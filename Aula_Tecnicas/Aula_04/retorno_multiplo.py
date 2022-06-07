def calc_soma_produto(num1: int, num2:int) -> tuple[int, int]:
    soma = num1 + num2
    produto = num1 * num2
    return soma, produto

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo numero: "))

soma, produto = calc_soma_produto(num1, num2)
print("A soma eh: ", soma)
print("o produto eh: ", produto)