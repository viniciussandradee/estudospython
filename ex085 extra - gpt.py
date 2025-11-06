#🎯 Enunciado:
#Crie um programa que permita ao usuário digitar vários números (quantos quiser).
#O programa deve:
#Armazenar todos os números em uma única lista com duas sublistas:
#uma para pares, outra para ímpares.
#No final, mostre:
#a quantidade de números digitados em cada categoria;
#e todos os valores de cada uma, usando um for com enumerate para percorrer as sublistas.

numeros = [[], []]
while True:
    valores = int(input('Digite aqui o valor: '))
    if valores % 2 == 0:
        numeros[0].append(valores)
    else:
        numeros[1].append(valores)
    pergunta = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if pergunta == 'N':
        break

numeros[0].sort()
numeros[1].sort()
for i, lista in enumerate(numeros):
    if i == 0:
        tipo = 'pares'
    else:
        tipo = 'impares'

print(f'Os números pares digitados são {numeros[0]}')
print(f'Os números ímpares digitados são {numeros[1]}')
