import functools

numbers = [1,2,3,4]

#reduce solo devuelve un valor, no necesito transformarlo a una lista
#lambda recibimos dos variables counter(incrementa el valor) y el item(que va iterando). por eso sumamos los dos (counter + item) y ,numbers le decimo la lista que vamos a iterar
result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)

def accum(counter, item): 
    print('counter => ', counter)
    print('item => ', item)
    return counter + item

result_v2 = functools.reduce(accum, numbers)
print(result_v2)    