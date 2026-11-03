def Quicksort_opt(vector, low=0, high=None):
    """
    Forma Otimizada do algoritmo de ordenação Quicksort,
    utiliza a mediana de 03 como escolha do pivot, assim distribuindo melhor as chamadas,
    utiliza o i, j como ponteiros para reduzir o uso de memoria em disco.
    
    Complexidades:
    Pior Caso: O(n2)
    Caso Médio, Melhor Caso = O(n log n)

    Conclusão:
    O Objetivo dessa abordagem é Fugir do Pior Caso e Reduzir o uso de Memória.
    """
    if high is None:
        high = len(vector) - 1

    if low >= high:
        return vector

    mid = len(vector) // 2
    if vector[low] > vector[mid]:
        vector[low], vector[mid] = vector[mid], vector[low]
    if vector[low] > vector[high]:
        vector[low], vector[high] = vector[high], vector[low]
    if vector[mid] > vector[high]:
        vector[mid], vector[high] = vector[high], vector[mid]

    vector[mid], vector[high - 1] = vector[high - 1], vector[mid]
    pivot = vector[high - 1]

    i = low + 1
    j = high - 2

    while True:
        while vector[i] < pivot:
            i += 1
        while vector[j] > pivot:
            j -= 1

        if i >= j: 
            break

        vector[i], vector[j] = vector[j], vector[i]
        i += 1
        j -= 1

    vector[i], vector[high - 1] = vector[high - 1], vector[i]

    Quicksort_opt(vector, low, i - 1) # Organiza a metade direita
    Quicksort_opt(vector, i + 1, high) # Organiza a metade esquerda

    return vector