#Exercício 87:
#Aprimore o desafio anterior, mostrando no final.
#a) A soma de todos os valores pares digitados;
#b) A soma dos valores da terceira coluna;
#c) O maior valor da segunda linha.

matriz = [[], [], []]
soma_pares = 0
for linha in range (3):
    for coluna in range (3):
        valor = int(input(f'Digite o valor para posição: [{linha}, {coluna}]: '))
        matriz[linha].append(valor)
for linha in matriz:
    for num in linha:
        print(f'{num:3}', end = ' ')
        if num % 2 == 0:
            soma_pares += num

    print()
soma = (matriz[0][2] + matriz[1][2] + matriz[2][2])
print('-=' * 30)
print(f'A soma dos valores pares são: {soma_pares}')
print('-=' * 30)
print(f'A soma dos valores da terceira coluna é: {soma}')
print('-=' * 30)
print(f'O maior valor da segunda linha foi: {max(matriz[1])}')
print('-=' * 30)