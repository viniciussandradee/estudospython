#Exercício 58:
#Melhore o jogo do desafio 028 onde o computador vai “pensar” um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar,
#mostrando no final quantos palpites foram necessários para vencer.

import random
contador = 0
usuario = 0
numero = random.randint(0,10)
while usuario != numero:
    usuario = int(input('Digite um número entre 0 e 10: '))
    contador += 1
    if usuario < numero:
        print('Mais... Tente novamente')
    else:
        print('Menos... Tente novamente')
if usuario == numero:
    print('Parabéns, você acertou!')
print(f'Foram necessárias {contador} tentativas para acertar!')