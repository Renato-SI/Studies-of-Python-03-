from random import shuffle  # Não Necessário!

# Algoritmo utilizado para ordenação de elementos, com base no menor elemento selecionado
# Existe outras maneiras mais eficientes
def buscarMenor(arr):
    """
    Encontra o menor elemento de uma lista.
    Percorre a lista comparando seus elementos e retorna
    o índice onde o menor elemento está localizado.
    Complexidade: O(n)
    """
    menor = arr[0]
    menor_index = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_index = i

    return menor_index

def ordenacaoporSelecao(arr):
    """
    Ordena uma lista utilizando o algoritmo de seleção.
    A cada iteração, encontra o menor elemento da lista,
    remove-o da lista original e adiciona-o ao final de
    uma nova lista.
    Complexidade: O(n²)
    """
    novo_arr = []
    for i in range(len(arr)):
        menor = buscarMenor(arr)
        novo_arr.append(arr.pop(menor))

    return novo_arr

# Apenas para testar em listas grandes!
teste = []
for j in range(1, 1001):
    teste.append(j)

shuffle(teste)
print(ordenacaoporSelecao(teste))