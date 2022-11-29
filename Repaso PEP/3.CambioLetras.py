
#Construya un programa que reciba por teclado un string cualquiera y 
# que entregue el string cambiando todas las ‘a’ por ‘i’. 
#Ejemplo:  entrada → hola, cómo estás?    salida → holi, cómo estis?

#Datos de entrada
texto = input("Ingrese un texto para cambiar las letras a por i: ")
print("Texto de entrada: ",texto)

#Procesamiento
textoNuevo= ""
i = 0
while i < len(texto):
    if texto[i] == "a":
        textoNuevo = textoNuevo + "i"
    else:
        textoNuevo = textoNuevo + texto[i]
    i +=1
#Datos de salida
print(textoNuevo)
