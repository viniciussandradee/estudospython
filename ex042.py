#Exercício 42:
#Refaça o desafio 35 dos triângulos,
#acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes

n1 = float(input('Digite medida 1: '))
n2 = float(input('Digite medida 2: '))
n3 = float(input('Digite medida 3: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n3 + n2 > n1:
    print('Sim, podemos formar um triângulo com as medidas informadas')
    if n1 == n2 == n3:
        print('O triângulo formado será Equilátero')
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('O triângulo formado será o Escaleno')
    else:
        print('O triângulo formado será o Isósceles')
else:
    print('Não é possível formar um triângulo com as medidas informadas')
