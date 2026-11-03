def Quicksort(vetor):
    """
    Implementação do Algoritmo de Ordenação QuickSort que utiliza o Método (Dividir para Conquistar)

    Complexidade:

    Pior Caso: O(n^2)
    Caso Médio = O(n log n)
    Melhor Caso = O(n log n)
    """
    if len(vetor) <= 1:
        return vetor

    pivo = vetor[0]
    lower, equal, high = [], [], []

    for elemento in vetor:
        if elemento < pivo:
            lower.append(elemento)

        elif elemento == pivo:
            equal.append(elemento)

        else:
            high.append(elemento)

    return Quicksort(lower) + equal + Quicksort(high)

teste = Quicksort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
print(teste)