"""
Ejercicio 10:
Escriba una función segundo_maximo(l) que reciba una lista de números l y retorne el segundo número más grande de la lista. Por ejemplo, para la lista [1,3,7,5], la función deberá retornar 5.


"""




def segundo_max(lista):
    
    
    maximo = max(lista)
    
    segundo=0
    
    
    for num in lista:
        if num>segundo and num<maximo:
            segundo=num
            
            
    return segundo


print(segundo_max([121,8,120,7]))