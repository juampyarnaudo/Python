'''
Funciones de set:
add(): Añade un elemento.
update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.
discard(): Elimina un elemento y si ya existe no lanza ningún error.
remove(): Elimina un elemento y si este no existe lanza el error “keyError”.
pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.
clear(): Elimina todo el contenido del conjunto.
'''

set_countries = {'col', 'mex', 'bol'}
print (set_countries)

#de que tamaño es el conjunto
size = len(set_countries) #3
print(size)

print('col' in set_countries) # True
print('pe' in set_countries) # False

#add _ agregar
set_countries.add('pe')
print(set_countries)
#lo duplico y lo mismo aparece uno solo
set_countries.add('pe')
print(set_countries)

# update
set_countries.update({'ar','ecua','pe'})
print(set_countries)

# remove
set_countries.remove('col')
print(set_countries)
#si quiero eliminar un elemnto que no existe me aparece un error
#set_countries.remove('arg')
set_countries.remove('ar')
print(set_countries)
#con discard se puede eliminar pero no importa si no existe, no tira error.
set_countries.discard('arg')

#limpiar el conjunto, borrar todo
set_countries.clear()
print(set_countries)
