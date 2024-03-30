def remover_repetidos(nums):

  unique_elements = set()
  for num in nums:
    unique_elements.add(num)
  return list(unique_elements)

lista1 = [1, 1, 2, 3, 3, 4]

print(remover_repetidos(lista1))