'''numbers = [1,2,3,4,5]
#crea una nueva lista con los elementos que hacen parte de esa condicion ( x%2==0)
new_numbers = list(filter(lambda x: x % 2 == 0, numbers ))
print(new_numbers)
'''

def filter_by_legth(words):
    new_list = list(filter(lambda x: len(x) > 3, words))

    return new_list

words = ['amor', 'sol', 'piedra', 'dia']
response = filter_by_legth(words)
print(response)

response_v2 = list(filter(lambda x: len(x) > 3, words))
print(response_v2)
'''
no_vegano = []
vegano = ['papas', 'tomate']
comidas = ['pollo', 'carne', 'papas']
lista_vegano = list(filter(lambda x: x == comidas, vegano))

print(lista_vegano) 

'''