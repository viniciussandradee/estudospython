def linha(tam= 30):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())

def menu():
    menu = (['VER CADASTRO', 'ADICIONAR NOME', 'SAIR DO PROGRAMA'])
    for i, v  in enumerate(menu, start= 1):
        print(f'[{i}] {v}')
    print(linha())

    while True:
        pergunta = (input('Digite sua escolha: ')).strip()

        if pergunta.isdigit():
            pergunta = int(pergunta)
        else:
            print('Valor Incorreto.')
            continue

        if 1 <= pergunta <= len(menu):
            break
        else:
            print('Valor Inválido')
    return pergunta




