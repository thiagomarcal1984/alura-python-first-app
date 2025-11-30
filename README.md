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
