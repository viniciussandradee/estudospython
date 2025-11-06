#Exercício 86:
#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]
for linha in range (3):
    for coluna in range (3):
        valor = int(input(f'Digite o valor para posição: [{linha}, {coluna}]: '))
        matriz[linha].append(valor)
for linha in matriz:
    for num in linha:
        print(f'{num:3}', end = ' ')
    print()


