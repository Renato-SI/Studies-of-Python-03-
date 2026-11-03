def Quicksort(vetor):
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