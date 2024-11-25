"""
Ejercicio 15:
Escriba una función suma_potencia(p) que reciba un número entero positivo p y calcule la suma de los dígitos de 2p. Por ejemplo, si p es 4, entonces 2^4 = 16 y la suma de los dígitos es 1 + 6 = 7.
"""


def potencia(pnt):
    
    valor=2**pnt
    resultado=0
    for n in str(valor):
        resultado+=int(n)
    
    
    
    return resultado



print(potencia(8))