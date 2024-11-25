"""
Ejercicio 8:
Escriba una función filtra_pares(n) que reciba como entrada un número entero positivo n y devuelva como salida otro número donde cada dí­gito par estará reemplazado por el dí­gito 1. Por ejemplo, si el número de entrada es 30852, la función deberá retornar 31151.

"""


def filtra_pares(n):
    
    
    n=str(n)
    
    
    for num in n:
        if int(num)%2==0:
            n=n.replace(num,'1')
            
            
    return n


print(filtra_pares(2222))
    
    