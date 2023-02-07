file = open('./text.txt')

#file.read() es para leer todo el archivo completo
#print(file.read())
#.readline() vamos a leer lineas x lineas. (es mas liviano)
'''
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
'''

for line in file:
    print(line)

#es importante cerrar el archivo cuando dejemos de utilizar. asi liberamos espacio de memoria.
file.close()

#con with -> de esta forma, automaticamente se cierra nuestro archivo cuando terminan las ejecuciones.
with open('./text.txt') as file:
    
    for line in file:
        print(line)
