#para ver el SO
import sys
print(sys.path)
#expresiones reguales
import re
text = 'Mi numero de telefono 311 123 121, codigo del pais es 57, mi numero de la suerte es 7'
#con una expresion regual podemos obtener los numeros de ese string
#findall para buscar todo
#y la sintaxis seria: encuentre todos los numeros 0-9 y le ponemos el + para que encuentre todos.
result = re.findall('[0-9]+',text)
print(result)

#modulo Hora  - fecha
import time
timestamp = time.time()
#obtenemos la hora y fecha
local_time = time.localtime()
#la pasamos a un formato legible
result_time = time.asctime(local_time)
print(timestamp)
print(result_time)

import collections
numbers = [1,1,1,2,3,4,2,1,2,5,4,3,2]

counter = collections.Counter(numbers)
print(counter) #Counter({1: 4, 2: 4, 3: 2, 4: 2, 5: 1})
#4 veces encontro el 1, 4 veces encontro el 2... y así
