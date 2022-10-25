
#ENTRADAS: int(número)
#SALIDAS: int(factorial)
#OBJETIVO: calcular factorial de un número n
def fact(n):
    #Caso base
    if n == 1:
        return 1

    #Recursión
    else:
        return n * fact(n-1)

print(fact(5))
