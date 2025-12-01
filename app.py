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
    os.system('cls') # Use 'clear' para Linux/Mac
    print('Finalizando o app.\n')

def opcao_invalida():
    print('Opção inválida! Tente novamente.')
    input('Digite ENTER para continuar...')
    os.system('cls')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novo restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'Restaurante "{nome_restaurante}" cadastrado com sucesso!')
    input('Digite ENTER para voltar ao menu principal...')
    os.system('cls')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Listandoo os restaurantes:\n')
    for restaurante in restaurantes:
        print(f'. {restaurante}')
    input('\nDigite ENTER para voltar ao menu principal...')
    os.system('cls')
    main()

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
