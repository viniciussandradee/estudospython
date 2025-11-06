#Exercício 43:
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do Peso
#Entre 18.6 e 25: Peso Ideal
#26 até 30: Sobrepeso
#31 até 40: Obesidade
#Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em m: '))
imc = peso / (altura ** 2)
print('-' * 20)
print(f'Seu IMC calculado é de: {imc:.1f}')
print('-' * 20)

if imc < 18.5:
    print(f'Você está ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print('Você está em SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Cuidado! Você está OBESO!')
else:
    print('OBESIDADE MÓRBIDA! Procure auxílio médico emergencial!')