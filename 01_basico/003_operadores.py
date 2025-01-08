#Operadores aritméticos python 
"""

Os operadores aritméticos são usados para calculos matematicos como adição, subtração, divisão, multiplicação entre outros.

"""

# + Adição
adicao = 10 + 35
print(f"Resultado Adição = {adicao}\n")

# - Subtração
subtracao = 10 - 5
print(f"Resultado Subtração = {subtracao}\n")

# * Multiplicação
multiplicacao = 5 * 10
print(f"Resultado Multiplicação = {multiplicacao}\n")

# / Divisão
divisao = 10 / 3
print(f"Resultado Divisão = {divisao}\n")

# // Divisão inteira
divisao_inteira = 10 // 3
print(f"Resultado Divisão inteira = {divisao_inteira}\n")

# % Resto da divisão
resto_divisao = 10 % 3
print(f"Resultado Resto da divisão = {resto_divisao}\n")

# ** Exponenciação
exponenciacao = 10 ** 2
print(f"Resultado Exponenciação = {exponenciacao}\n")

"""
Ordem de procedencia

1 = Parenteses 

2 = Exponenciação

3 = Multiplicação, Divisão, Divisão inteira, e resto da divisão

4 = Adição e Subtração
"""

resultado = 10 + 2 * 3  # 16 (multiplicação antes da adição)

resultado = (10 + 2) * 3  # 36 (parênteses primeiro)

#! Falar sobre operadores de comparação