# Hacer el siguiente programa:
# Dado el nombre de una criptomoneda (por ejemplo, bitcoin, ethereum, etc)
# solicitar el monto en USDT invertido
# la cantidad de la criptomoneda comprada
# el valor de la criptomoneda al momento de la compra
# la fecha de compra
import re
from datetime import datetime


nombre_crypto = str(input("Ingrese el nombre de la criptomoneda (ejemplo: bitcoin, ethereum): "))
monto_invertido = int(input("Ingrese el monto en USDT invertido: "))
valor_crypto_compra = float(input("Ingrese el valor de la criptomoneda al momento de la compra: "))
fecha_compra = datetime.now().strftime("%d/%m/%Y")

cantidad_crypto_comprada = round(monto_invertido / valor_crypto_compra, 5)

print("\nResumen de la inversión:")
print(f"Criptomoneda: {nombre_crypto}")
print(f"Monto invertido (USDT): {monto_invertido}")
print(f"Cantidad comprada: {cantidad_crypto_comprada}")
print(f"Valor al momento de la compra: {valor_crypto_compra} USDT")
print(f"Fecha de compra: {fecha_compra}")
print("\n¡Inversión registrada con éxito!")

archivo = open("./ejemplo.txt", "a", encoding="utf-8")

# Escribir
archivo.write(f"\nFecha de compra: {fecha_compra}\n")
archivo.write(f"Criptomoneda: {nombre_crypto}\n")
archivo.write(f"Monto invertido (USDT): {monto_invertido}\n")
archivo.write(f"Valor al momento de la compra: {valor_crypto_compra} USDT\n")
archivo.write(f"Cantidad comprada: {cantidad_crypto_comprada}\n")
archivo.close()


print("\nContenido del archivo 'ejemplo.txt':")
archivo = open("./ejemplo.txt", "r", encoding="utf-8")
# Leer el archivo
contenido = archivo.read()
print(contenido)

archivo.close()

