
def par_impar(vetor):
    vetor.sort(reverse=True)
    pares = 0
    impares = 0
    for i in vetor:
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    print("Pares:", pares)
    print("Ímpares:", impares)

lista1 = [1, 1, 2, 3, 3, 4]

par_impar(lista1)