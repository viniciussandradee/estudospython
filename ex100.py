#Exercício 100:
#Faça um programa que tenha uma LISTA chamada números e DUAS FUNÇÕES
#chamada SORTEIA() e SOMAPAR(). A primeira função vai sortear 5 números
#e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos
#os valores PARES sorteados pela função anterior.

from random import randint

valores = []

def sorteia():
    valores.clear()
    numeros = [randint(0,10) for _ in range (10)]
    valores.extend(numeros)
    print('Os números sorteados foram:', end= ' ')
    for v in valores:
        print(f'{v}', end = ' ')
    print()

def somapar():
    soma = 0
    print('A soma dos números pares é: ',)
    for v in valores:
        if v % 2 == 0:
            soma += v
    print(f'{soma}')

def somaimpar():
    somaimpar = 0
    print('A soma dos números ímpares é: ')
    for v in valores:
        if v % 2 == 1:
            somaimpar += v
    print(f'{somaimpar}')

def media():
    print('A média dos valores é: ')
    media = sum(valores) / len(valores)
    print(f'{media:.2f}')


while True:
    sorteia()
    print('-' * 20)
    somapar()
    print('-' * 20)
    somaimpar()
    print('-' * 20)
    media()
    print('-' * 20)
    perguntar = str(input('Você deseja selecionar outros números [S/N]? ')).strip().upper()[0]
    if perguntar == 'N':
        print('Obrigado por participar!')
        break