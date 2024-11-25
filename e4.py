"""
Ejercicio 4:
Escriba una función primeros_divisores(n) que reciba como entrada un número entero positivo n y devuelva como salida una lista con los primeros 5 divisores (como máximo) de n. Por ejemplo, si el número de entrada es 24, la función deberá retornar la lista [1,2,3,4,6]. Tenga en cuenta que hay números que pueden tener menos de 5 divisores. Por ejemplo, los divisores de 8 son 1, 2, 4 y 8, por lo que la función deberá retornar la lista [1, 2, 4, 8].


"""

def p_div(n):
    
    lista=[1]
    
    for num in range(2,n+1):
        
        if n%num==0:
            lista.append(num)
            
        if len(lista)==5:
            break
    
    
    return lista


print(p_div(10))