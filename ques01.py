def selection_sort(vetor):
    n = len(vetor)

    for i in range(n):
        id_minimo = i
        for j in range(i + 1, n):
            if vetor[id_minimo] > vetor[j]:
                id_minimo = j
        temp = vetor[i]
        vetor[i] = vetor[id_minimo]
        vetor[id_minimo] = temp

    return vetor

lista1 = [1, 5, 3, 2, 4]

selection_sort(lista1)

print(lista1)