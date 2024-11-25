"""
Ejercicio 14:
Escriba una función producto_triple(l) que reciba una lista de números de tres dígitos l y retorne True si al menos un producto de tres dígitos termina en 2 o False en caso contrario. Por ejemplo, para la lista [253, 341, 613] deberá retornar True, ya que 3×4×1 = 12 termina en 2. En cambio, para [253, 342, 613] deberá retornar False, ya que ningun producto termina en 2.

"""



def producto(lista):
    
    for num in lista:
        calculo=1
        for n in str(num):
            calculo*=int(n)
        if str(calculo).endswith('2'):
            return True
    
    return False 


print(producto([253,342,613]))