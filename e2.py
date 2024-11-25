"""

Ejercicio 2:
Escriba una función cuenta_pares(n) que reciba como entrada un número entero positivo n y devuelva como salida el número de dígitos pares que contiene. Por ejemplo, si el número de entrada es 123204, la función deberá retornar 4. Recuerde que el 0 es par.


"""



def pares(n):
    if n<0:
        return "Deben ser numeros positivos"
    
    cantidad_pares=0
    
    
    for num in str(n):
        if int(num)%2==0:
            cantidad_pares+=1
            
            
    return cantidad_pares



print(pares(57))
