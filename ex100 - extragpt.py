from random import randint

valores = []
def linha():
    print('-' * 30)

def sorteia():
    valores.clear()
    numeros = [randint(0,10) for _ in range (10)]
    valores.extend(numeros)
    print('Os números sorteados foram:', end= ' ')
    for v in valores:
        print(f'{v}', end = ' ')
    print()

def somapar():
    if not valores:
        print('Nenhum número foi sorteado ainda!')
        return
    soma = 0
    print('A soma dos números pares é: ',)
    for v in valores:
        if v % 2 == 0:
            soma += v
    print(f'{soma}')

def somaimpar():
    if not valores:
        print('Nenhum número foi sorteado ainda!')
        return
    somaimpar = 0
    print('A soma dos números ímpares é: ')
    for v in valores:
        if v % 2 == 1:
            somaimpar += v
    print(f'{somaimpar}')

def media():
    if not valores:
        print('Nenhum número foi sorteado ainda!')
        return
    print('A média dos valores é: ')
    media = sum(valores) / len(valores)
    print(f'{media:.2f}')

menu = """
=====================
    MENU PRINCIPAL
=====================
[1] SORTEAR NÚMEROS
[2] SOMAR PARES
[3] SOMAR ÍMPARES
[4] MÉDIA
[5] SAIR DO PROGRAMA
"""
while True:
    print(menu)
    resposta = input('Digite sua escolha: ').strip()
    if resposta == '5':
        print('Obrigado por participar. Volte Sempre!')
        break
    elif resposta == '4':
        media()
        linha()
    elif resposta == '3':
        somaimpar()
        linha()
    elif resposta == '2':
        somapar()
        linha()
    elif resposta == '1':
        sorteia()
        linha()
    else:
        print('Opção Inválida. Tente Novamente')