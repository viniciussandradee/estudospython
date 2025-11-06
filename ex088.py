#Exercício 88:
#Faça um programa que ajude um jogador da MegaSena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo numa lista composta

from random import randint
import time
print('-=' * 30)
print(f'{'Jogo da Mega Sena':^40}')
print('-=' * 30)

palpites = []
jogo = int(input('Quantos jogos deseja fazer? '))
print()
print(f'Gerando {jogo} jogos...')
print('-=' * 20)

for c in range(jogo):
    temp = []
    for _ in range(6):
        valor = randint(1, 60)
        temp.append(valor)
    temp.sort()
    palpites.append(temp[:])

for i, c in enumerate(palpites, start= 1):
    time.sleep(0.5)
    print(f'Jogo {i}: {c}')
print('-' * 30)
print(f'{'BOA SORTE!':^20}')
print('-' * 30)