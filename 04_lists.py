'''
numbers = []
numbers2 = []


for element in range(1, 11):
  numbers.append(element)
print(numbers)

for element in range(1, 11):
  numbers2.append(element * 2)
print(numbers2)

numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)
#el mismo ejemplo, pero agregando * 2
numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)

'''
#LIST COMPREHENSION
#es una forma de generar listas con sintaxis mas corta.

numbers = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers.append(i * 2)
print(numbers)

numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)
