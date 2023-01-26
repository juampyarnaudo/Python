#recibe un parametro x, le aumentamos +1 y devuelve el resultado
def increment(x):
    return x + 1
increment_v2 = lambda x: x + 1

# funcion, recibe un parametro y el 2do parametro es una funcion (x + func), donde la funcion recibe un parametro X
def high_ord_func(x, func):
    return x + func(x) 
high_ord_func_v2 = lambda x, func: x + func(x) 
result = high_ord_func(2, increment)
#2 + (2 + 1) = 5
print(result)

#def func (args) :
# return ret_val
#func = lambda args: ret_val

result = high_ord_func_v2(2,increment_v2)
print(result)