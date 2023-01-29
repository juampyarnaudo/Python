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

#agrego un nuevo atributo (taxes) al diccionario
def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

#para que los elementos del array items no se modifiquen creamos una copia en otro array

def add_taxes_v2(item):
    new_item = item.copy()
    new_item['taxes'] = item['price'] * .19
    return new_item

new_items = list(map(add_taxes_v2,items))
print('Nueva lista')
print(new_items)
print('Lista vieja')
print(items)