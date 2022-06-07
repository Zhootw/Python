def maisum(num: int) -> int:
    return num + 1

numeros = [1, 2, 3, 4, 5]
somados = map(maisum, numeros)
for num in somados:
    print(num)