#Exercício 71:
#Crie um programa que simule o funcionamento de um CAIXA ELETRÔNICO.
#No início, pergunte ao usuario qual o valor ser sacado (número inteiro) e o
#programa vai informar quantas cédulas de cada valor serão entregues.
#Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cedulas = [50, 20, 10, 1]
saque = int(input('Qual valor deseja sacar? R$ '))
i = 0
print('-=' * 20)
print('Você receberá:')
while saque > 0 and i < len(cedulas):
    qtd = saque // cedulas[i]
    if qtd > 0:
        print(f'{qtd} cédulas de R$ {cedulas[i]}')
    saque = saque % cedulas[i]
    i += 1
print('-=' * 20)
print('Obrigado por usar o Caixa Eletrônico. Volte Sempre!')
print('-=' * 20)