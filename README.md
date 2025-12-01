# Manipulação de strings
## Para saber mais: The Zen of Python
Fora de ordem, as só pra priorizar o estudo do Zen do Python:
```bash
# Texto do The Zen of Python por Tim Peters:
python -c "import this"
```

Resultado do "The Zen of Python" traduzido para português:
```
* Bonito é melhor que feio.
* Explícito é melhor que implícito.
* Simples é melhor que complexo.
* Complexo é melhor que complicado.
* Plano é melhor que aninhado.
* Esparso é melhor que denso.
* Legibilidade conta.
* Casos especiais não são especiais o bastante para quebrar as regras.
* Embora praticidade vença a pureza.
* Erros nunca devem passar silenciosamente.
* A menos que sejam explicitamente silenciados.
* Diante da ambiguidade, recuse a tentação de adivinhar.
* Deveria haver uma — e preferencialmente só uma — maneira óbvia de fazer algo.
* Embora essa maneira possa não ser óbvia a princípio a menos que você seja holandês.
* Agora é melhor que nunca.
* Embora nunca seja frequentemente melhor que agora mesmo.
* Se a implementação é difícil de explicar, é uma má ideia.
* Se a implementação é fácil de explicar, pode ser uma boa ideia.
* Namespaces são uma grande ideia — vamos fazer mais dessas!
```
## Primeiro programa
Programa inicial para exibir as opções do aplicativo backend "Sabor Express":

```python
# app.py
print('Sabor Express\n')

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair')
```

## Boas práticas
Em Python, usamos os seguintes padrões:

1.  `snake_case` para variáveis;
2. `PascalCase` para classes;
3. `SCREAMING_SNAKE_CASE` para constantes.

Código atualizado do arquivo `app.py`:
```python
# app.py
print('Sabor Express\n')

# Resto do código

opcao_escolhida = int(input('Escolha uma opção: '))

print('Opção escolhida:',  opcao_escolhida)
```
## Interpolação de String
Aspas triplas para criar strings grandes com quebras de linha.

> Visite o site https://fsymbols.com/ para criar textos formatados para linha de comando.

É possível usar strings formatadas (as chamadas f-strings). Para isso, prefixe a string com a letra `f` e depois interpole variáveis/retornos de função usando chaves para chamar a variável/função. Por exemplo: 
```python
print(f'Opção escolhida: {opcao_escolhida}')
```

Mudança no arquivo `app.py`:

```python
# Perceba as aspas triplas com quebras de página.
print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
1. Cadastrar restaurante
2. Listar restaurante
3. Ativar restaurante
4. Sair
""")

opcao_escolhida = int(input('Escolha uma opção: '))

# Perceba a interpolação de variável com a f-string.
print(f'Opção escolhida: {opcao_escolhida}')
```
# Módulos e funções
## If else
Blocos de if..elif..else no Python:

```python
# app.py
if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    print('Encerrando o programa.')
```
## Tipo int e str
A função `type` mostra o tipo de valor da variável:
```python
print(type(input("Entrada: "))) # retorna <class 'str' >
print(type(1)) # retorna <class 'int' >
```

Para converter uma string para inteiro, use a função `int`:
```python
opcao_escolhida = int(input('Escolha uma opção: '))
```

## Funções e import
Para definir funções no Python, use:
```python
def funcao():
    comandos
```

Para importar uma biblioteca (por exemplo, a de interação com o sistema operacional) use a palavra reservada `import` seguida da biblioteca que você deseja importar:
```python
import os
```

Código do arquivo `app.py`:

```python
# Resto do código
def finalizar_app():
    os.system('cls') # Use 'clear' para Linux/Mac
    print('Finalizando o app.\n')
    
if opcao_escolhida == 1:
    # Resto do código
else:
    finalizar_app()
```

## Aprofundando em funções
Primeiro: o Python usa o dunder `__name__` para armazenar o nome do módulo importado. Se o módulo não tiver sido importado, então o returno do dunder `__name__` é a string `__main__`. Isso facilita a identificação do programa principal e evita sua execução caso o arquivo do programa principal seja importado.

Veja o código: 
```Python
if __name__ == '__main__':
    main()
```
Note que dentro do bloco `if` é chamada a função `main`, que contém a lógica do programa principal.

O código do arquivo `app.py` foi modularizado em diferentes funções, para melhorar a legibilidade:
```python
import os 

def exibir_nome_do_programa():
    # Resto do código

def exibir_opcoes():
    # Resto do código

def finalizar_app():
    # Resto do código

def escolher_opcao():    
    # Resto do código

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
```
## Para saber mais: instrução match
A partir da versão 3.10 do Python surgiu a instrução `match`, que funciona como o switch/case de outras linguagens.

De acordo com a documentação, a instrução tem a seguinte sintaxe: 

```python
match status:
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case _: # Opção default
        print("Something's wrong with the internet")
```
O código do arquivo `app.py` foi modificado para usar a instrução `match`:
```python
# Resto do código
def escolher_opcao():    
    opcao_escolhida = int(input('Escolha uma opção: '))

    print(f'Opção escolhida: {opcao_escolhida}')

    match opcao_escolhida:
        case 1:
            print('Cadastrar restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurante')
        case _:
            finalizar_app()
# Resto do código
```
## Hora da prática: condicionais
```python
def par_impar():
    """
    1 - Solicite ao usuário que insira um número e, em seguida, use uma 
    estrutura if else para determinar se o número é par ou ímpar.
    """
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')

def classificar_idade():
    """
    2 - Peça ao usuário para inserir sua idade e use uma estrutura if, elif,
    else para classificar a pessoa como "Criança" (0-11 anos), "Adolescente" 
    (12-17 anos) ou "Adulto" (18 anos ou mais).
    """
    idade = int(input('Digite sua idade: '))
    if idade < 12:
        print('Criança')
    elif 12 <= idade < 18:
        print('Adolescente')
    elif idade >= 18:
        print('Adulto')
    else:
        print('Valor inválido')

def login():
    """
    3 - Solicite um nome de usuário e uma senha e use uma estrutura if else 
    para verificar se o nome de usuário e a senha fornecidos correspondem aos 
    valores esperados determinados por você.
    """
    usuario = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')
    nome_esperado = 'admin'
    senha_esperada = '1234'

    if usuario == nome_esperado and senha == senha_esperada:
        print('Acesso concedido.')
    else:
        print('Acesso negado.')

def quadrantes():
    """
    4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e 
    utilize uma estrutura if elif else para determinar em qual quadrante do 
    plano cartesiano o ponto se encontra de acordo com as seguintes condições:
    - Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
    - Segundo Quadrante: o valor de x < 0 e o valor de y > 0;
    - Terceiro Quadrante: os valores de x e y devem ser menores que zero;
    - Quarto Quadrante: o valor de x < 0 e o valor de y < 0;
    - Caso contrário: o ponto está localizado no eixo ou origem.
    """
    x = float(input("Digite a coordenada x: "))
    y = float(input("Digite a coordenada y: "))

    if x > 0 and y > 0:
        print('Primeiro quadrante')
    elif x < 0 and y > 0:
        print('Segundo quadrante')
    elif x < 0 and y < 0:
        print('Terceiro quadrante')
    elif x > 0 and y < 0:
        print('Quarto quadrante')
    else:
        print('O ponto está localizado no eixo ou origem.')


if __name__ == '__main__':
    # par_impar() #1
    # classificar_idade() #2
    # login() #3
    quadrantes() #4
```

# Listas, laços e exceções
## Try except
Foco na sintaxe do `try... except`:

```python
try:
    # Código que pode lançar exceção.
except:
    # Código do tratamento da exceção.
```
> Note que o tipo de exceção não precisa ser declarado depois de `except`, embora seja recomendado.

Mudanças no código de `app.py`:
```python
# Resto do código
def escolher_opcao():    
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Opção escolhida: {opcao_escolhida}')

        # Resto do código
    except:
        opcao_invalida()
# Resto do código
```
## Listas
Foco no comando de acréscimo de elementos na lista (método `append` da lista):

```python
minha_lista = []
lista.append('Novo item')
print(lista) 
# Resultado: 
# ['Novo item']
```
Mudanças no arquivo `app.py`:
```python
# Resto do código
restaurantes = []

# Resto do código
def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novo restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'Restaurante "{nome_restaurante}" cadastrado com sucesso!')
    input('Digite ENTER para voltar ao menu principal...')
    os.system('cls')
    main()

# Resto do código
```
## Laço de repetição for
Foco nas iterações com for:
```python
for item in lista:
    print(item)
```
Mudanças no arquivo `app.py`:
```python
def listar_restaurantes():
    os.system('cls')
    print('Listandoo os restaurantes:\n')
    for restaurante in restaurantes:
        print(f'. {restaurante}')
    input('\nDigite ENTER para voltar ao menu principal...')
    os.system('cls')
    main()
```
