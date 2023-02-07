import random
countries = ['col', 'mex', 'bol', 'pe']

population_v2 = {i:random.randint(1, 100) for i in countries }
print(population_v2)

#generar otro diccionario con paises > 50
result = { country: population for (country, population) in population_v2.items() if population > 50 }
print(result)

text = 'Hola, soy Juampi'
#es para obtener una letra vocal ('aeiou') (la c=caracter) y pasarla a mayuscula
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)