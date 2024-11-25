"""
Ejercicio 13:
Escriba una función rota_derecha(l, p) que reciba una lista de números l y un número entero p, y retorne una nueva lista rotada hacia la derecha p veces. La rotación a la derecha es el desplazamiento de los elementos de la lista a una posición a la derecha y la copia del último elemento al primero. Por ejemplo, para [1,2,3,4,5] y 1, la versión rotada hacia la derecha sería [5,1,2,3,4]. Y para [1,2,3,4,5] y 2, la versión rotada hacia la izquierda sería [4,5,1,2,3]. Asuma que p es mayor o igual que 0 y menor que la longitud de la lista l.



"""


def rotar_d(lista,p):
    
    resultado=[0]*len(lista)
    
    for i,el in enumerate(lista):
        nuevo_indice=(p+i)%len(lista)
        resultado[nuevo_indice]=el
        
        # [1,2,3,4,5] = len(lis)=5
        # i=0 p=1  -> i+p = 0+1 = 1 % 5 = 1
        # i=1 p=1  -> (1 + 1) %5=2
        # i=1 p=28 ->(1+28)=29%5=4
 
    return resultado

print(rotar_d([1,2,3,4,5],28))
    
    