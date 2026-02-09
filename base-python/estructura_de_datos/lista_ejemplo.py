# Ordenada 
# Mutable (la podés modificar) 
# Permite elementos duplicados
frutas = ["manzana", "banana", "pera", "Frutilla", "Mango", "Pomelo"]

print(f"Listar  frutas:  {frutas}")

# Agregar
frutas.append("naranja")

# Acceder
print(frutas[0])  # manzana

# Modificar
frutas[1] = "banana madura"

# Recorrer
for f in frutas:
    print(f)

# Largo
print(len(frutas))


bebida = ["agua", "jugo", "gaseosa", "jugo de limon", "agua mineral"]
comida = ["pizza", "hamburguesa", "ensalada", "pasta"]

cena = [bebida, comida]
print(cena)
print(cena[0][1])  # jugo
print(cena[1][2])  # ensalada

