#Exercício 41:
#A Confederação Nacional de Natação precisa de um programa que leia
#o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SÊNIOR
#Acima: MASTER

from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('-' * 20)
print(f'Idade Registrada: {idade}')
print('-' * 20)
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 20:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER')
