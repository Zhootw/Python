def ler_salarios(n_salarios: int) -> list:
    listapessoas = []

    for i in range (n_salarios):
        nome = input(f'Digite o nome da pessoa {i+1}: ')
        idade = int(input(f'Digite a idade da pessoa {i+1}: '))
        salario = float(input(f'Digite o salario da pessoa {i+1}: '))

        pessoa = {'nome': nome, 'idade': idade, 'salario': salario}
        listapessoas.append(pessoa)

        return listapessoas