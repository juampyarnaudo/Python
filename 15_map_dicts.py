items = [
    #diccionarios
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'sombrero',
        'price': 150
    }
]

#transformar una lista que me devuelva solos los precios
#
prices = list(map(lambda item: item['price'], items))
print(prices)