"""
Ejercicio 1:
Escriba una función frecuencia_digitos(n) que reciba como entrada un número entero positivo n y devuelva como salida una lista de 10 números donde cada número deberá indicar la cantidad de veces que aparece cada dígito en el número. Por ejemplo, si el número de entrada es 913294207820, la función deberá retornar la lista [2,1,3,1,1,0,0,1,1,2], ya que hay dos 0, un 1, tres 2, un 3, un 4, ningún 5, ningún 6, un 7, un 8 y dos 9.                          0 1 2 3

"""



def frec_dig(n):
    
    if n < 0:
        return []
    
    lista=[0]*10
    # [0]*10 = [0,0,0,0,0,0,0,0,0,0]
    
    
    for num in str(n):
        lista[int(num)]+=1
        
    
    return lista




print(frec_dig(913294207820))
    
    
    
    
    
    
    
    