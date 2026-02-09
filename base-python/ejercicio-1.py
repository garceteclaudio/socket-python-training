
############################################# if, elif, else
edad = 19

if edad < 18:
    print("Eres menor de edad.")
elif edad == 11:
    print("Tienes 11 años.")
else:
    print("Eres mayor de edad.")

############################################# input
print("Ingresa un número:")
numero = int(input())
print(f"El número ingresado es: {numero}")

print("Ingresa tu nombre:")
nombre = str(input())
print(f"Tu nombre es: {nombre}")

#### manipular cadenas

texto = "Hola, Mundo!"
print(texto.lower())      # hola, mundo!
print(texto.upper())      # HOLA, MUNDO!
print(texto.replace("Mundo", "Python"))  # Hola, Python!
print(texto.split(","))   # ['Hola', ' Mundo!']
print(texto.strip("!"))   # Hola, Mundo
print(texto.find("Mundo")) # 6
print(texto.startswith("Hola")) # True
print(texto.endswith("!"))  # True


############################################# Ejemplo tipos de for

#Recorre cada elemento de la lista.
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)

# Se usa cuando querés repetir algo un número de veces.
for i in range(5):
    print(i)

#  range(inicio, fin, paso)
for i in range(1, 10, 2):
    print(i)

# Ejemplo sencillo de bucle for con break, continue y pass
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero == 3:
        continue  # Salta la iteración cuando numero es 3, no imprime 3
    elif numero == 7:
        break  # Detiene el bucle cuando numero es 7, no procesa más números
    elif numero % 2 == 0:
        pass  # No hace nada, pero permite la estructura del if
    else:
        print(f"Número impar: {numero}")  # Imprime solo números impares que no son 3