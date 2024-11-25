"""
Ejercicio 11:
Escriba una función indices_especiales(s) que reciba una cadena s y retorne una lista de índices correspondientes a las posiciones de los caracteres especiales de s. Recuerde que un caracter especial es aquel no es ni una letra ni un dígito, por ejemplo: '*', ' ', '_', etc. Entonces, si la cadena de entrada es 'abc 123*_567', la función deberá retornar [3,7,8].


"""



def in_esp(texto:str):
    
    resultado=[]
    
    for i,c in enumerate(texto):
        if not c.isalnum():
            resultado.append(i)
            
    return resultado



print(in_esp("abc$% 123*_567"))
            
    
    
    