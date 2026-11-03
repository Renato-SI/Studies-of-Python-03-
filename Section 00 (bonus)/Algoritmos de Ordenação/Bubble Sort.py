def Bublesort(vetor):
    n = len(vetor)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                swapped = True

        if not swapped:
            break
    return vetor

teste = Bublesort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
print(teste)