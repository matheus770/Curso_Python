from utils import *


palavra_completa = False
lista_de_palavras = ["MAÇA", "BANANA", "MACACO"]

palavra_lista_atual, qtd_letras_palavra = contar_letras(lista_de_palavras[2])
lista_palavra_preenchida = palavra_lista_atual[:]

print(palavra_lista_atual, qtd_letras_palavra)

while palavra_completa == False:
    menu_palavra(palavra_lista_atual)
    letra_usuario = str(input("Digite uma letra: "))
    lista_palavra_preenchida = verifica_se_existe_letra(lista_de_palavras[2], letra_usuario, palavra_lista_atual)
    if lista_palavra_preenchida != palavra_lista_atual:
        palavra_lista_atual = lista_palavra_preenchida[:]
    else:
        print("letra nao existe na palavra")