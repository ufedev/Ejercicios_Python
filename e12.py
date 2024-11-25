"""
Ejercicio 12:
Escriba una función rota_izquierda(l, p) que reciba una lista de números l y un número entero p, y retorne una nueva lista rotada hacia la izquierda p veces. La rotación a la izquierda es el desplazamiento de los elementos de la lista a una posición a la izquierda y la copia del primer elemento al último. Por ejemplo, para [1,2,3,4,5] y 1, la versión rotada hacia la izquierda sería [2,3,4,5,1]. Y para [1,2,3,4,5] y 2, la versión rotada hacia la izquierda sería [3,4,5,1,2]. Asuma que p es mayor o igual que 0 y menor que la longitud de la lista l


"""

def rotar(lista,cant):

    return lista[cant:] + lista[:cant]



# 
# [1,2,3,4,5], 2 -> [3,4,5] + [1,2] -> 

print(rotar([1,2,3,4,5],2))