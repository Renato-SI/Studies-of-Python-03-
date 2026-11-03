def Shellsort(vetor):
    n = len(vetor)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            chave = vetor[i]
            j = i

            while j >= gap and vetor[j - gap] > chave:
                vetor[j] = vetor[j - gap]
                j -= gap

            vetor[j] = chave

        gap //= 2

    return vetor

teste = Shellsort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
print(teste)

