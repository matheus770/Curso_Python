"""
Variaveis são usadas para armazenar dados que podem ser acessados e manipulados posteriormente no programa.

Em python não precisamos declarar o tipo de dado da variavel pois ela é uma linguagem de tipagem dinamica.

Atribuimos valor a variavel com o operador de atribuição =
"""

nome = "Seu nome" # Esta variavel se chama nome e esta recebendo o valor "Seu nome" que tem o tipo de string

"""
Python possui alguns tipos de dados embutidos, vou mostrar os que mais uso:

string = Cadeia de caracteres ou caractere unico envolvido de aspas simples ou duplas Ex: "Alex", 'Sabrina'

int = Numeros inteiros Ex: 6, 1000, -8

float = Numeros de ponto flutuante Ex: 3.14, 100.65, -1.56
É interessante ressaltar que no python a virgula (,) conhecida no sistema brasileiro para separar numeros decimais é o (.)

boolean = Valores logicos, poder ser apenas True ou False Ex: camisa_existe = True

None = Valor usado para representar a ausencia de valor ou vazio Ex: camisa_existe = None
"""

nome_livro = 'A fuga dos ratos' #String

idade = 25 #int

salario = 124.25 #float

esta_de_camisa = True #boolean

celular_quebrou = False #boolean

cesto_de_roupas = None #none type

"""
Boas praticas

* O nome da variavel deve começar com uma letra. porem pode ser usado letra ou underscore (_)

* Variaveis que começam com numeros não são permitidas

* Não pode ser usado as palavras reservadas da linguagem Ex: 
*  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
*  'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
*   'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
*   'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

* Certifiquise que as variaveis estão na mesma caixa de tamanho, para o python, livro pode ser diferente de Livro. Aconselho a nomear variaveis sempre em caixa baixa.

* Não é permitido usar espaço no nome de variaveis, use sempre o underscore para simular um espaço na nomeação
* Exemplo Certo: cor_da_camisa = 'Azul' 
* Exemplo Errado: cor da camisa = 'Azul' 

* Apenas o underscore de caractere especial pode ser usado na nomeação de variaveis

* Escolha nomes que reflitam o proposito da variavel

* Use sempre que der snake_case, palavras separadas por underscore, assim o codigo fica padronizado e melhor de se entender com variaveis bem descritas

* Evite nomes de uma letra, exceto em casos de loops ou calculos matematicos.

"""

# Agora podemos juntar o print com as variaveis para exibir os resultados de uma forma mais dinamica 

#Existe duas formas de concatenarmos variaveis em prints uma é essa com .format(variavel) apos as aspas e a outra é colocando f depois do print e antes das aspas.
# Lembrando que sempre deve ter as mascaras de substituição {} para funcionar. 
print("O meu nome é {}".format(nome))

print(f'A minha idade é {idade}')

print(f'Meu nome é {nome} e minha idade é {idade}')