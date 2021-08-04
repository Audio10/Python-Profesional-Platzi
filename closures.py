"""
Reglas
    Debe tener una nested function.
    La nested function debe referenciar un valor de un scope superior.
    La funcion que envuelve a la nested function debe retornarla tambien (La nested function).
"""


def make_multiplier(x):

    def multiplier(n):
        return x * n

    return multiplier


times10 = make_multiplier(10)
times4 = make_multiplier(4)

# Si eliminas la funcion aun se sigue referenciando gracias al closure
del(make_multiplier)
print(times10(3))
print(times4(5))
print(times10(times4(2)))
