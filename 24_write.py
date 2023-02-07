#utilizando 'r+' estoy dando permiso de lectura - escritura
#y con .write puedo escribir en la linea final.
#con 'w+' va a reescribir todo el archivo.
with open('./text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('\nnuevas cosas en este archivo')
    file.write('\nOtra linea')
    file.write('\nOtra mas! ')


