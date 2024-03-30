def max(array):
  elemento_max = array[0]
  for elemento in array:
    if elemento > elemento_max:
      elemento_max = elemento
  return elemento_max

def min(array):
  elemento_min = array[0]
  for elemento in array:
    if elemento < elemento_min:
      elemento_min = elemento
  return elemento_min

lista1 = [1, 5, 3, 2, 4]
maior = max(lista1)
menor = min(lista1)

print("Maximum element:", maior)
print("Minimum element:", menor)


