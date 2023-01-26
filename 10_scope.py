price = 100 # alcance global

def increment():
    #creamos una nueva varible con un alcance local (price)
    price = 200
    price = price + 10
    return price

print(price)
price2 = increment()
print(price2)

def increment():
    #creamos una nueva varible con un alcance local (price)
    price = 200
    result = price + 10
    return result
#no puedo imprimir result, porque fue creada dentro de una funcion.
#print(result)