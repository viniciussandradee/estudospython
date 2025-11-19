def arquivoexiste(nome):
    try:
        open(nome, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True

def criaarquivo(nome):
    try:
        a = open(nome, 'wt')
    except Exception:
        print('Falha ao criar o arquivo. Verifique! ')
    else:
        a.close()
        print('Arquivo Criado com Sucesso! Bom trabalho')

def lerarquivo(arq):
    from sis_cad import interface
    interface.cabecalho('VER CADASTRO')

    try:
        a = open(arq, 'rt')
    except Exception:
        print('Erro ao ler arquivo.')
        return

    for linha in a:
        partes = linha.strip().split(';')
        n = partes[0].strip()
        i= partes[1].strip()
        print(f'Nome: {n:<20} Idade:{i} anos')

    a.close()