def Selectsort(vetor):
    n = len(vetor)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[menor]:
                menor = j 
        vetor[i], vetor[menor] = vetor[menor], vetor[i]

    return vetor

teste = Selectsort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
print(teste)