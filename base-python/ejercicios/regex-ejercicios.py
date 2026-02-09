import re

print("\n-------- REGEX - Expresiones regulares")

# Buscar un valor específico en el texto
texto = "Monto invertido (USDT): 2000"
resultado = re.search("2000", texto)
print(resultado.group())


# Buscar un patrón específico en el texto: El numero luego del texto "Monto invertido (USDT):"
texto = "Monto invertido (USDT): 2000"
monto = re.search(r"Monto invertido \(USDT\):\s*(\d+)", texto)

print(monto.group(1))


# Buscar todos los montos en el texto
texto = """
Monto invertido (USDT): 2000
Monto invertido (USDT): 1000
Monto invertido (USDT): 500
"""

montos = re.findall(r"Monto invertido \(USDT\):\s*(\d+)", texto)
suma_montos = 0
for elemento in montos:
    suma_montos += int(elemento)

print(montos)
print(suma_montos)


# Buscar todos los nombres
texto = """
Nombre: Player One
Nombre: Player Two
Nombre: Player Three
Nombre: Player Four
Nombre: Player Five
Nombre: Player Six

"""

nombres = re.findall(r"Nombre:\s*(\w+ \w+)", texto)
print(nombres)
