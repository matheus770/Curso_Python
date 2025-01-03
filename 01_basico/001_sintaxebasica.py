# Este é um comentario em python. Utilizado para comentar uma linha geralmente.

"""
Este Tambem é um comentario em python, Utilizado para comentar trechos de codigos. 
Comentarios tem grande utilidade em um codigo bem desenvolvido, algumas delas são:

* Documentar o Código
* Fornecer informações adicionais de uma parte especifica do codigo
* Ajudar outros desenvolvedores entender sua logica de codigo
* Ajudar a lembrar do que foi feito no passado do codigo
* Tornar o codigo mais legivel consequentemente mais facil de dar manutenção no futuro
"""

# Indentação

""" 
A indentação serve para indicar a estrutura e o escopo do código, é essencial para o bom funcionamento do código.

Regras:

* O recuo padrão é de 4 espaços no python
* A primeira linha do codigo não pode conter recuo
* Todas linhas dentro de um bloco de codigo devem estar no mesmo nivel de recuo 
Exemplo errado:
if 5>4:
print("é maior")
else:
print("é menor")

Exemplo certo:
if 5>4:
    print("é maior")
else:
    print("é menor")
"""

# Função print()

"""
A função print é uma de varias funções que já vem embutidas no python, é uma das funções mais utilizadas.
Ela serve para exibir informações no console/terminal, servindo tambem para depuração de codigo.

A sintaxe dela é bem simples: 

print("A informação que voce quer exibir aqui")
Aspas simples tambem pode ser utilizado
print('A informação que voce quer exibir aqui')
"""

# Exemplo de uso
print("Olá amigo!")

print('Olá amigo!')
print('Tudo bem?')

# O \n pode ser usado para pular linha mantendo a escrita no mesmo print
print('Olá amigo! \nTudo bem?')

# O uso de aspas triplas no print serve para exibir trechos maiores de informação
print("""
Olá amigo!
Tudo bem ?
Vamos programar hoje ?
    """)