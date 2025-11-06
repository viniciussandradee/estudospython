#Exercício 59:
#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] SOMAR
#[2] MULTIPLICAR
#[3] MAIOR
#[4] NOVOS NÚMEROS
#[5] SAIR
#Seu programa deverá realizar a operação solicitada em cada caso.

opcoes = ['1', '2', '3', '4', '5']
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
while True:
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR')

    escolha = input('Digite sua escolha: ')
    if escolha == '5':
        print('Saindo do Jogo! Até breve!')
        break
    if escolha not in opcoes:
        print('Entrada Inválida. Tente Novamente')
        continue
    if escolha == '1':
        print(f'A soma de {n1} e {n2} é igual {n1 + n2}')
    elif escolha == '2':
        print(f'Multiplicando {n1} e {n2} o resultado é {n1 * n2}')
    elif escolha == '3':
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n2 > n1:
            print(f'O maior número é {n2}')
        else:
            print(f'Os números {n1} e {n2} possuem valores iguais')
    elif escolha == '4':
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        print(f'Novos Números solicitados: {n1} e {n2}')
    print('-=' * 7)