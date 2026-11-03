def Quicksort_opt2(vector):
    """
    O Objetivo dessa Abordagem Otimizada é Fugir dos Piores Casos,
    ainda que seja possível cair neles. Para isso, selecionei o pivot através da mediana de 3,
    uma estratégia que visa separar melhor as comparações das chamadas recursivas.
    
    Complexidade:
    Pior Caso: O(n^2)
    Caso Médio = O(n log n)
    Melhor Caso = O(n log n)

    """
    n = len(vector)
    if n <= 1:
        return vector

    low, mid, high = 0, (n // 2), (n - 1)

    if vector[low] > vector[mid]:
        vector[low], vector[mid] = vector[mid], vector[low]
    if vector[low] > vector[high]:
        vector[low], vector[high] = vector[high], vector[low]
    if vector[mid] > vector[high]:
        vector[mid], vector[high] = vector[high], vector[mid]

    pivo = vector[mid]

    lower, equal, higher = [], [], []
    for element in vector:
        if element < pivo:
            lower.append(element)
        elif element > pivo:
            higher.append(element)
        else:
            equal.append(element)

    return Quicksort_opt2(lower) + equal + Quicksort_opt2(higher)

teste = Quicksort_opt2([9, 8, 7, 7, 8, 6, 5, 4, 3, 2, 1, 0])
print(teste)