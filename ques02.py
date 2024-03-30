def selection_sort_custom_key(vetor, chave):
    n = len(vetor)

    for i in range(n):
        id_minimo = i
        for j in range(i + 1, n):
            if chave(vetor[id_minimo]) > chave(vetor[j]):
                id_minimo = j
        temp = vetor[i]
        vetor[i] = vetor[id_minimo]
        vetor[id_minimo] = temp

    return vetor


def crescente(x):
    return x


def decrescente(x):
    return -x


lista1 = [1, 5, 3, 2, 4]

selection_sort_custom_key(lista1, crescente)
print("Lista ordenada em ordem crescente:", lista1)

selection_sort_custom_key(lista1, decrescente)
print("Lista ordenada em ordem decrescente:", lista1)
