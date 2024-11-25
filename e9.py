"""
Ejercicio 9:
Escriba una función combina_unicos(a, b) que reciba dos listas de números, a y b, y retorne una nueva lista formada por la concatenación de a y b pero incluyendo sólo una vez aquellos elementos re-petidos. Por ejemplo, para [1,2,3,1,2] y [2,4,5,6,4], la función deberá retornar [1,2,3,4,5,6].



"""
import collections


def combina_unicos(a,b):
    
    lista=a+b
    resultado=[]
    for num in lista:
        if num not in resultado:
            resultado.append(num)
    
    return resultado


print(combina_unicos([1,2,3,1,2],[2,4,5,6,4]))

