"""
Em python temos a função input() que serve para capturar dados fornecidos pelo usuário e armazenar em variaveis para que possamos usar posteriormente no codigo.

* De forma padrão os dados capturados pela função são armazenados como string porém podemos converter eles para os outros tipo conforme necessitamos
"""
ano_atual = 2025

ano_nascimento_usuario = input("Em que ano voce nasceu: ")
print(f'O usuario nasceu no ano {ano_nascimento_usuario} e o tipo da variavel é {type(ano_nascimento_usuario)}') # tipo string

#Com a função type() podemos exibir o tipo de dado da variavel desejada, isso é muito util para o desenvolvimento do codigo pois se tentarmos fazer calculo com string vai dar erro.

"""
Podemos converter manualmente de duas formas, ou direto no input ou na operação que quisermos fazer, por exemplo nesse caso queremos descobrir a idade do usuario.
"""

# Forma direto no input 
"""
Desta forma precisamos identificar o tipo desejado para o calculo e colocar ele antes da função input()

* Deve notar que vamos usar a mesma variavel, e o valor que vai prevalescer nela vai ser sempre o ultimo atribuido. fica a dica caso use variaveis com o mesmo nome.
"""
ano_nascimento_usuario = int(input("Em que ano voce nasceu: "))
print(f'O usuario nasceu no ano {ano_nascimento_usuario} e o tipo da variavel é {type(ano_nascimento_usuario)}') # tipo inteiro
calculo_idade = ano_atual - ano_nascimento_usuario
print(f'O usuario nasceu no ano {ano_nascimento_usuario} e tem aproximadamente {calculo_idade} anos')

# Forma direto na função de calculo
ano_nascimento_usuario = input("Em que ano voce nasceu: ")
print(f'O usuario nasceu no ano {ano_nascimento_usuario} e o tipo da variavel é {type(ano_nascimento_usuario)}') # tipo string
# calculo_idade = ano_atual - ano_nascimento_usuario || Desta vez se executarmos o calculo desse jeito vai dar erro pois nao se pode calcular string com int ou float
# se quiser testar desative o comentario e execute o codigo
# podemos utilizar o tipo desejado englobando a variavel desejada dentro dos parenteses do tipo.
calculo_idade = ano_atual - float(ano_nascimento_usuario)
print(f'O usuario nasceu no ano {ano_nascimento_usuario} e tem aproximadamente {calculo_idade} anos')
# Se reparar o calculo da variavel ano atual com o tipo int e o ano de nascimento com o tipo float funcionou e prevaleceu o tipo float.
# Entre int e float o python sempre vai prevaleer o tipo float como padrão.
# python faz isso para garantir precisão no calculo pois se o valor resultasse em algo fracionado com o tipo int isso seria perdido. 