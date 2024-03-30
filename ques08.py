def mediana(vetor):
  vetor.sort()
  if len(vetor) % 2 == 1:
    return vetor[len(vetor) // 2]
  else:
    return (vetor[len(vetor) // 2] + vetor[len(vetor) // 2 - 1]) / 2

lista1 = [1, 1, 2, 3, 4]

print(mediana(lista1))
