#Exercício 39:
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar no serviço militar
#Se é a hora de ele se alistar
#Se já passou o tempo de alistamento.
#Seu programa também deverá informar o tempo que falta ou o prazo que já passou.

from datetime import date
nasc = int(input('Digite a data de seu nascimento: '))
atual = date.today().year
idade = atual - nasc
print('--' * 20)
print(f'Idade registrada: {idade} anos')
print('--' * 20)
if idade < 18:
    falta = 18 - idade
    previsao = atual + falta
    print(f'Você ainda não precisa se alistar!')
    print(f'Faltam {falta} anos')
    print(f'Seu alistamento será {previsao}')
elif idade == 18:
    print('Procure a Junta Militar! Você deve se alistar!')
else:
    atraso = idade - 18
    previsao = atual - atraso
    print('Dispensado!')
    print(f'A {idade - 18} anos você se alistava!')
    print(f'Seu alistamento foi em {previsao}.')