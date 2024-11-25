"""
Ejercicio 3:
Escriba una función invierte_impares(n) que reciba como entrada un número entero positivo n y devuelva como salida otro número que contenga únicamente los dígitos impares de n pero en orden inverso. Por ejemplo, si el número de entrada es 2741309, la función deberá retornar el número 9317.

"""



def inv_impares(n):
    
    resultado=""
    
    for num in str(n):
        if int(num)%2!=0:
            resultado+=num # 91

    return resultado[::-1]


print(inv_impares(13579))
    
    
