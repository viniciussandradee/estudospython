#Exercício 82:
#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores
#pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das 3 listas geradas.

lista = []
pares = []
impares = []

while True:
    num = (int(input('Digite um valor: ')))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    pergunta = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if pergunta == 'N':
        break

print(f'Os números digitados foram: {lista}')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')


