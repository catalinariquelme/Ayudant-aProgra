nterms = int(input("How many terms? "))

# Numeros base
n1, n2 = 0, 1
count = 0

# Verificar si los terminos son positivos
if nterms <= 0:
   print("Ingrese un número positivo")

# Caso base = 1
elif nterms == 1:
   print("Fibonacci secuencia upto",nterms,":")
   print(n1)

# Genera secuencia
else:
   print("Fibonacci secuencia:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # Actualiza variables
       n1 = n2
       n2 = nth
       count += 1