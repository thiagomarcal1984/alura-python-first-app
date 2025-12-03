import os 

restaurantes = [
    { 'nome': 'Praça', 'categoria' : 'Japonesa', 'ativo' : False },
    { 'nome': 'Pizza Suprema', 'categoria' : 'Pizza', 'ativo' : True },
    { 'nome': 'Cantina', 'categoria' : 'Italiano', 'ativo' : False },
]

def exibir_nome_do_programa():
    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    print("""
    1. Cadastrar restaurante
    2. Listar restaurante
    3. Alternar estado do restaurante
    4. Sair
    """)

def finalizar_app():
    exibir_subtitulo('Finalizando o app.')

def voltar_ao_menu_principal():
    input('\nDigite ENTER para voltar ao menu...')
    os.system('cls')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    print('Opção inválida! Tente novamente.')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novo restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante "{nome_restaurante}": ')
    dados_do_restaurante = {
        'nome': nome_restaurante,
        'categoria': categoria_restaurante,
        'ativo': False,
    }
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante "{nome_restaurante}" cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    print(f'{"Nome Restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'ativado' if restaurante["ativo"] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_restaurante.lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            estado_atual = 'ativo' if restaurante['ativo'] else 'inativo'
            print(f'O restaurante "{restaurante["nome"]}" agora está {estado_atual}.')
    if not restaurante_encontrado:
        print(f'Restaurante "{nome_restaurante}" não encontrado.')
    voltar_ao_menu_principal()

def escolher_opcao():    
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Opção escolhida: {opcao_escolhida}')

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
