import os 

restaurantes = ['Pizza', 'Sushi', 'Hamburguer']

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
    3. Ativar restaurante
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
    print(texto)
    print()

def opcao_invalida():
    print('Opção inválida! Tente novamente.')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novo restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'Restaurante "{nome_restaurante}" cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes:')
    for restaurante in restaurantes:
        print(f'. {restaurante}')
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
                print('Ativar restaurante')
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
