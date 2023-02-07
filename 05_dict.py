'''
dict = {}
for i in range(1,5):
  dict[i] = i * 2
print(dict)

dict_v2 = {i: i * 2 for i in range(1,5)}
print(dict_v2)
'''
'''
#importo la libreria random
import random

countries = ['col', 'mex', 'bol', 'pe']
population =  {}
for i in countries:
  population[i] = random.randint(1, 100)
print(population)

population_v2 = {i:random.randint(1, 100) for i in countries }
print(population_v2)

'''
#hacer un algoritmo que convierta estas dos listas en un diccionario
names = ['nico', 'zule', 'santi']
ages = [12,56,98]

#se hace una lista con tuplas
print(list(zip(names, ages)))
#creamos el diccionario
new_dict = {name: age for (name, age) in zip(names,ages)}
print(new_dict)


