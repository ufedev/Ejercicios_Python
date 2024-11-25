"""
Ejercicio 5:
Escriba una función vocales_frase(s) que reciba como entrada una frase s y devuelva como salida una lista de números donde cada número deberá indicar la cantidad de vocales que hay en cada palabra de la frase. Por ejemplo, si la frase de entrada es 'Say no more', la función deberá retornar la lista [1,1,2], ya que hay una vocal en la primera palabra, una vocal en la segunda palabra y dos vocales en la tercera palabra.


"""


def voc_f(frase):
    
    
    
    resultado=[] 
    vocales=["a",'e','i','o','u']
    contador=0
    for caracter in frase.lower():
        if caracter==" ":
            resultado.append(contador)
            contador=0
        
        if caracter in vocales:
            contador+=1
        
    
    resultado.append(contador)
    
    return resultado



print(voc_f("Federico Malfasi"))
