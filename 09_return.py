
#a la función puedo enviar por defecto =1 en el caso de que no agregue un valor.
def find_volume(length=1,width=1,depth=1):
    return length * width * depth, width, 'hola'
#si quiero enviar solamente el width, pongo ese valor=10    
result = find_volume(width=10)
print(result)

#si retornamos masde un valor con , nos va a devolver una tupla

#en el caso de que quiera solamente el valor de la posición 0, pongo [0]
print(result[0])

result2, width, text = find_volume(width=10)
print(result2)
print(width)
print(text)

