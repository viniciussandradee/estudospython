#Exercício 76:
#Crie um programa que tenha uma tupla única com os nomes de produtos e seus
#respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma TABULAR.

tupla = ('Tabaco', 18, 'Filtro', 10, 'Seda', 4, 'Piteira', 7, 'Isqueiro', 6)
print(f'{'Produto':<30}{'Preço':>10}')
print('-=' * 20)
print(f'{'LISTAGEM DE PRODUTOS:':^40}')
print('-=' * 20)
for i in range(0, len(tupla), 2):
    protudo = tupla[i]
    preco = tupla[i + 1]
    print(f'{protudo:.<30}R${preco:>10.2f}')
print('-=' * 20)
