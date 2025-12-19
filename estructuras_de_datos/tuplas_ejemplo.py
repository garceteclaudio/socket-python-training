
#Ordenada
#Ocupan menos memoria que una lista
#Son inmutables, no se pueden cambiar → seguras
#Ideales para datos fijos (coordenadas, colores, configuraciones)
#Más rápida que una lista

punto = (10, 20)
print(punto[0])  # 10


mi_tupla = ("Juan", 30, True, 1.75)
print(mi_tupla)

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numeros)

# Desempaquetado de tuplas (muy útil)
x, y = (10, 20)
print(x)  # 10
print(y)  # 20

#Tupla anidada (tuplas dentro de tuplas)
matriz = (
    (1, 2),
    (3, 4),
    (5, 6)
)

print(matriz[1][0])  # 3

# Tuplas como retorno múltiple de funciones
def calcular():
    return (10, 20)

a, b = calcular()
print(a, b)