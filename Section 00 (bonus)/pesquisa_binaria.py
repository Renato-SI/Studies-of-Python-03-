# Algoritmo Utilizado para Busca de maneira otimizada, em listas ordenadas de quaisquer n elementos.

# Exemplo:
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [0, 1, 3, 5, 9, 10, 15, 18]
print(pesquisa_binaria(minha_lista, 5)) # Vai retornar 3, que é a posição do item 5 nba lista
print(pesquisa_binaria(minha_lista, 80)) # Vai retornar None, o item não está na lista