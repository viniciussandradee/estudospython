from sis_cad import interface, cadastro, arquivo
import time

def iniciar_sistema():
    arq = 'cadastro.txt'
    if not arquivo.arquivoexiste(arq):
        arquivo.criaarquivo(arq)

    while True:
        interface.cabecalho('SISTEMA DE CADASTRO')
        escolha = interface.menu()
        interface.linha(30)

        if escolha == 1:
            interface.linha(30)
            print(f'{"Nome":<30}{"Idade":>30}')
            interface.linha(30)
            arquivo.lerarquivo(arq)

        elif escolha == 2:
            cadastro.cadastrar(arq)

        elif escolha == 3:
            print('Saindo...')
            time.sleep(0.5)
            print('Até logo')
            break
        else:
            print('Opção Inválida!')



