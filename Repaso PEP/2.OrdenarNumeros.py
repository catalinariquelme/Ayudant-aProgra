#Construya un programa que identifique el número más alto dentro de una lista de elementos.
# Considere que puede que no todos los elementos sean válidos.

#DATOS DE ENTRADA

lista = []
print("Para terminar escriba end")
n = input("Ingrese un número: ")

# Entradas (end = no más entradas)
while n != "end":
    if n != "end":
        lista.append(n)
        n = input("Ingrese otro numero: ")
i = 0

#PROCESAMIENTO
#Verificador
while i < len(lista):
    lista[i] = int(lista[i])
    i += 1    
j =0

#Se muestra por pantalla la lista a procesar
print("Los números a analizar son:",lista)

#Se ordenan los números de menor a mayor
while j < len(lista)-1:
    i = 0
    while i < len(lista)-1:
        #Se comparan dos números
        if lista [i] > lista[i+1]:
            #Swap: intermabio de número
            lista.insert(i,lista.pop(i+1))
        i += 1
    j +=1
#Se almacena el ultimo de la lista
ultimoNumero = len(lista)-1

#SALIDA
print("EL numero mayor es",lista[ultimoNumero])
