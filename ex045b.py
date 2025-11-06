#Exercício 45:
#Crie um programa que faça o computador jogar JOKENPÔ
# (Pedra x Papel x Tesoura) com você.

import random
import time

opcoes = ['Pedra', 'Papel', 'Tesoura']

print('Vamos jogar JOKENPÔ')
print('-' * 30)
while True:
    print('\n[1] Pedra')
    print('[2] Papel')
    print('[3] Tesoura')
    print('[0] Sair do Jogo')

    escolha = (input('Qual a sua escolha? '))
    if escolha == '0' or escolha.lower() == 'sair':
        print('Saindo do jogo... Até a próxima')
        break

    if escolha not in opcoes:
        print('Escolha Inválida! Tente novamente!')
        continue

    computador = random.choice(opcoes)

    print('JO')
    time.sleep(0.5)
    print('KEN')
    time.sleep(0.5)
    print('PO')
    time.sleep(0.5)

    print(f'Você escolheu {escolha}')
    print(f'O computador escolheu {computador}\n')

    if escolha == computador:
        print('Empate')
    elif escolha == 'Pedra':
        if computador == 'Tesoura':
            print('Você venceu, Parabéns!')
        else:
            print('Computador Venceu!')
    elif escolha == 'Papel':
        if computador == 'Pedra':
            print('Você venceu, Parabéns!')
        else:
            print('Computador Venceu!')
    elif escolha == 'Tesoura':
        if computador == 'Papel':
            print('Você venceu, Parabéns!')
        else:
            print('Computador Venceu')
