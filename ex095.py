#Exercício 95:
#Aprimore o DESAFIO 93 para que ele funcione com VÁRIOS JOGADORES,
#incluindo um sistema de visualização de DETALHES DO APROVEITAMENTO
#de cada jogador.

atleta = {}
jogadores = []
while True:
    temp = []
    nome = str(input('Digite o nome do atleta: '))
    atleta['nome'] = nome
    partidas = int(input('Digite a quantidade de partidas: '))
    print('-=' * 15)
    gols = []
    for c in range(partidas):
        tentos = int(input(f'Quantos gols foram marcados na partida {c+1}: '))
        gols.append(tentos)
        atleta['totalgols'] = sum(gols)
        atleta['gols'] = gols
        jogadores.append(atleta.copy())
        print('-=' * 15)

    pergunta = input('Deseja Cadastrar mais jogadores [S/N]? ').strip().upper()[0]
    if pergunta == 'N':
        break
print('-=' * 30)
print('RESUMO DOS JOGADORES:')
print('-' * 30)
print(f'{"Código":<6}{"Nome":<15}{"Total de Gols":<15}')
for idx, g in enumerate(jogadores):
    print(f'{idx:<6}{g["nome"]:<15}{g["totalgols"]:<15}')
while True:
    print('-' * 30)
    pesquisa = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if pesquisa == 999:
        break
    if pesquisa >= len(jogadores) or pesquisa < 0:
        print('Erro! Código inválido.')
    else:
        jogador = jogadores[pesquisa]
        print(f'-- LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
        for i, gol in enumerate(jogador['gols']):
            print(f'    => Na partida {i+1}, fez {gol} gols.')
        print(f'Total de gols: {jogador["totalgols"]}')


