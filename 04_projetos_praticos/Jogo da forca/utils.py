def contar_letras(palavra: str) -> int:
    """
    Args:
    Returns:
    """
    qtd_letras = len(palavra.replace(" ", ""))
    lista_palavra_em_branco = ["_" for letra in palavra ]
    return lista_palavra_em_branco, qtd_letras

def menu_palavra(palavra: list) -> str:
    """_summary_

    Args:
        letras_palavra (int): _description_

    Returns:
        str: _description_
    """
    palavra_formatada = '.'.join([letra for letra in palavra])
    return print(palavra_formatada)

def verifica_se_existe_letra(palavra: str, letra_usuario: str, palavra_lista_atual: list) -> list:
    if letra_usuario.upper() in palavra.upper():
        posicao_letras = [indice for indice, letra in enumerate(palavra) if letra == letra_usuario] 
        nova_lista_palavra = palavra_lista_atual[:]

        for indice in posicao_letras:
            if 0 <= indice < len(nova_lista_palavra):
                nova_lista_palavra[indice] = letra_usuario

        return nova_lista_palavra 
    else:
        return palavra_lista_atual