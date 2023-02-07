# print ( 0 / 0)  -> ZeroDivisionError: division by zero
#print(result)   -> NameError: name 'result' is not defined
print('Hola')

suma = lambda x,y: x + y
assert suma (2,2) == 4


print('Hola 2')
age = 10
if age < 18: 
    raise Exception('No se permiten menores de edad')

