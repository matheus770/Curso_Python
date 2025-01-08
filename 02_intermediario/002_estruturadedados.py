"""
As estruturas de dados são fundamentais para armazenar, organizar e manipular dados de forma mais eficiente.
"""

#Principais Estruturas de dados
# Lista São estruturas mutáveis que armazenam multiplos itens em uma variavel
# Aceitam diferentes tipos de dados e permitem valores duplicados
"""
Metodos uteis:
append() = Adiciona um item a lista
remove() = Remove um item da lista
sort() =
pop() = 
index() =
"""

frutas = ['manga', 'laranja', 'maça']
frutas.append("uva")
print(frutas)

# Tuplas são imutaveis ou seja seus valores não podem ser alterados depois da definiçaõ da mesma
# geralmente são usadas para representar dados constantes 

coordenadas = [10,35]
print(coordenadas[1])

#Conjuntos Estruturas mutaveis mas não permitem nenhum valor duplicado
#Usadas para operações como união, interseção e Diferença
#Metodos úteis: add(), remove(), union(), intersection

numeros_pares = {2,4,6,4}
numeros_impares = {1,3,5,1}

print(numeros_pares)    #sem duplicados
print(numeros_impares)  #sem duplicados

#Dicionarios Estruturas mutaveis que armazenam pares de chaves e valor semelhante so json
#As chaves devem ser unicas mas os valores podem ser duplicados
#metodos uteis: keys(), values(), items(), get(), pop()

aluno = {"nome": "João", "idade": 20, "curso": "Python"}
print(aluno["nome"])  # Saída: João
aluno["idade"] = 21   # Atualiza o valor da idade

#List comprehension é uma maneira eficiente e legivel de criar listas em Python. Em vez de gerar loops grandes e desnecessarios para construir uma lista

#Sintaxe
# [expressão for item in iterável if condição]
# expressão define como cada elemento da lista sera gerado
# for item in iterável itera sobre um iteravel como uma lista,string ou range.
# if condição (opcional) filtra os itens com base na condição

#List comprehension simples
numeros = [x for x in range(10)]
print(numeros)  # Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehension com operação
quadrados = [x**2 for x in range(10)]
print(quadrados)  # Saída: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension com condições
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Saída: [0, 2, 4, 6, 8]

maiores_que_cinco = [x for x in range(10) if x > 5]
print(maiores_que_cinco)  # Saída: [6, 7, 8, 9]
 
# List comprehension com operação e condição
quadrados_pares = [x**2 for x in range(10) if x % 2 == 0]
print(quadrados_pares)  # Saída: [0, 4, 16, 36, 64]
 
# List comprehension com strings 
letras = [char for char in "Python"]
print(letras)  # Saída: ['P', 'y', 't', 'h', 'o', 'n']

maiusculas = [char.upper() for char in "python"]
print(maiusculas)  # Saída: ['P', 'Y', 'T', 'H', 'O', 'N']

# List Comprehension Aninhada
matriz = [[x * y for x in range(1, 4)] for y in range(1, 4)]
print(matriz)
# Saída:
# [
#   [1, 2, 3],  # 1*1, 1*2, 1*3
#   [2, 4, 6],  # 2*1, 2*2, 2*3
#   [3, 6, 9]   # 3*1, 3*2, 3*3
# ]
 

#List comprehension condicional 
par_ou_impar = ["par" if x % 2 == 0 else "ímpar" for x in range(10)]
print(par_ou_impar)  # Saída: ['par', 'ímpar', 'par', 'ímpar', ..., 'ímpar']


"""
Vantagens 
Sintaxe Compacta - Substitui múltiplas linhas de código por uma única linha.
Melhor Leitura - Torna o código mais direto e fácil de entender.
Performance - Geralmente mais rápido do que construir listas usando loops tradicionais.
"""