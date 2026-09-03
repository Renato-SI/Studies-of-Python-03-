"""
Realiza uma pesquisa binária recursiva em uma lista ordenada,
contabilizando a quantidade de comparações necessárias para
encontrar um elemento ou concluir que ele não está presente.

A entrada contém todos os valores em uma única sequência, onde
o primeiro elemento representa o valor a ser buscado e os demais
elementos representam a lista ordenada.

O índice central é definido de acordo com o tamanho do intervalo:
se for ímpar, utiliza-se o elemento central; se for par, utiliza-se
o primeiro elemento da segunda metade.
"""

def pesquisa_binaria(lista, inicio, fim, item, contador=0):
    if inicio > fim:
        return contador

    contador += 1
    meio = ((inicio + fim) // 2)

    if ((fim - inicio) + 1) % 2 == 0:
        meio += 1

    if lista[meio] == item:
        return contador

    elif lista[meio] > item:
        return pesquisa_binaria(lista, inicio, meio - 1, item, contador)

    else:
        return pesquisa_binaria(lista, meio + 1, fim, item, contador)

entrada = input('').split()
entrada = list(map(int, entrada))
n_alvo = entrada[0]
lista_final = entrada[1:]

print(pesquisa_binaria(lista_final, 0, len(lista_final) - 1, n_alvo))