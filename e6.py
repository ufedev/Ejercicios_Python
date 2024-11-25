"""
Ejercicio 6:
Escriba una función reemplaza_suma(l) que reciba como entrada una lista de números positivos de tres dígitos l y devuelva como salida otra lista donde cada número deberá reemplazarse por la suma de sus dígitos. Por ejemplo, si la lista de entrada es [271,139,310], la función deberá retornar [10,13,4], ya que 10 = 2 + 7 + 1, 13 = 1 + 3 + 9 y 4 = 3 + 1 + 0.
"""


def ree_suma(lista_nums):
    
    resultado=[]
    
    for num in lista_nums:
        suma=0
        for n in str(num):
            suma+=int(n)
        resultado.append(suma)
        
        
    return resultado



print(ree_suma([271,139,310]))
    