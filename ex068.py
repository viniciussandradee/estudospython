#Exercício 68:
#Faça um programa que jogue PAR ou ÍMPAR com o computador. O jogo só será INTERROMPIDO
# quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou ao final do jogo.

from random import randint
print('-=' * 10)
print(f'{'PAR OU IMPAR':^20}')
print('-=' * 10)

vitorias = 0
jogadas = 0

while True:
    n = int(input('Digite um valor: '))
    computador = randint(0,10)
    resultado = n + computador
    jogadas += 1

    pi = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    while pi not in ['P', 'I']:
        pi = input('Entrada Inválida. Digite apenas P ou Par e I ou Impar: ').strip().upper()[0]

    if resultado % 2 == 0 and pi == 'I':
        print(f'Jogador: {n} e o computador: {computador}. Resultado: {resultado}.\nComputador Venceu! Tente Novamente')
        break
    if resultado % 2 == 1 and pi == 'P':
        print(f'Jogador: {n} e o computador: {computador}. Resultado: {resultado}.\nComputador Venceu! Tente Novamente')
        break
    else:
        vitorias += 1
        print(f'Jogador: {n} e o computador: {computador}. Resultado: {resultado}. \nJogador Venceu!')
print(f'Foram {jogadas} jogadas, e o JOGADOR venceu {vitorias} vezes.')
