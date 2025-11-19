def cadastrar(arq):

    cadastro = []

    nome = str(input('Digite seu nome: ')).strip()
    while nome == '' or nome.isnumeric():
        print('Erro! Por favor, digite seu nome: ')
        nome = str(input('Digite seu nome: ')).strip()
    cadastro.append(nome)

    idade = input('Digite sua idade: ')
    while idade == '' or not idade.isdigit():
        print('Erro! Por favor, digite apenas números')
        idade = input('Digite sua idade: ')
    idade = int(idade)
    cadastro.append(idade)

    with open(arq, 'a') as arquivo:
        linha = cadastro[0] + ';' + str(cadastro[1]) + "\n"
        arquivo.write(linha)

    print(f'Novo registro de {cadastro[0]} adicionado com sucesso!')



