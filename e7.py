"""

Ejercicio 7:
Escriba una función forma_entero(d) que reciba como entrada un número decimal positivo d y devuelva como salida el número entero formado omitiendo el punto decimal. Por ejemplo, si el número de entrada es 91.467, la función deberá retornar 91467.


"""


def f_int(dec):
    
    dec=str(dec).split(".")
    
    
    return "".join(dec)



print(f_int(91.467))