def terceiro_maior(vetor):
  vetor.sort(reverse=True)
  if len(set(vetor)) == len(vetor):
    return vetor[2]
  else:
    for i in range(2, len(vetor)):
      if vetor[i] != vetor[i-1]:
        return print(vetor[i])
      
lista1 = [1, 1, 2, 3, 3, 4]

terceiro_maior(lista1)

