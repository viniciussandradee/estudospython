#Exercício 73:
#Crie uma TUPLA preenchida com os 20 primeiros colocados 4da Tabela do Brasileirão BETANO, na ordem de colocação. Depois mostre:
#a) Apenas os 5 primeiros colocados;
#b) Os últimos 4 colocados da tabela;
#c) Uma lista com os times em ordem alfabética (enumerate())
#d) Em que posição na tabela está o time CHAPECOENSE.

seriea = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 'Fluminense', 'Vasco da Gama', 'São Paulo', 'Bragantino', 'Corinthians', 'Grêmio', 'Ceará', 'Internacional', 'Atlético Mineiro', 'Santos', 'Vitória', 'Juventude', 'Fortaleza', 'Sport')
print('-=' * 20)
print(f'{'TABELA BRASILEIRÃO SERIE A':^40}')
print('-=' * 20)
for time in seriea:
    print(f'{time}', end = ' ')
print()
print('-=' * 20)
print('A) Os primeiros cinco colocados são: ')
for time in (seriea[:5]):
    print(f'{time} ', end = ' ')
print()
print('-=' * 20)
print('B) Os 4 últimos colocados são: ')
for time in (seriea[-4:]):
    print(f'{time} ', end = ' ')
print()
print('-=' * 20)
print('C) Em ordem Alfabética, os times ficam: ')
for time in sorted(seriea):
    print(f'{time} ', end = ' ')
print()
print('-=' * 20)
print('D) Posição do Time da Chapecoense: ')
if 'Chapecoense' in seriea:
    pos = seriea.index('Chapecoense') + 1
    print(f'O time da Chapecoense está em {pos}ª posição na tabela.')
else:
    print('O time da Chapecoense não se encontra no campeonato desse ano')


