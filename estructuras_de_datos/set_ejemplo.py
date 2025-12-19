#Un conjunto:
#No tiene orden
#No permite duplicados
#Es muy rápido para búsquedas

numeros = {1, 2, 3, 3, 4}

# Los duplicados se eliminan
print(numeros)

# Agregar
numeros.add(5)

# Eliminar
numeros.remove(2)

# Recorrer
for n in numeros:
    print(n)

# Ver si existe
print(3 in numeros)  # True
