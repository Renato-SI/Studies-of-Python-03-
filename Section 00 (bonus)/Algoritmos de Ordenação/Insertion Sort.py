def Insertionsort(vetor):
    n = len(vetor)
    for i in range(1, n):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1

        vetor[j + 1] = chave

    return vetor

teste = Insertionsort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
print(teste)