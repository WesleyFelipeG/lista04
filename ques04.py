def segundo_menor(vetor):
  vetor.sort()
  if len(set(vetor)) == len(vetor):
    return vetor[1]
  else:
    for i in range(1, len(vetor)):
      if vetor[i] != vetor[i-1]:
        return vetor[i]


lista1 = [1, 5, 3, 2, 4, 1]

print(segundo_menor(lista1))



