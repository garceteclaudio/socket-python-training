
#guarda datos clave → valor.

persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Buenos Aires"
}

# Acceder
print(persona["nombre"])

# Agregar nueva clave
persona["profesion"] = "Programador"

# Modificar
persona["edad"] = 31

# Recorrer (claves)
for clave in persona:
    print(clave, "=>", persona[clave])
