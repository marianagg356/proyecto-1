# Calculadora de Compras con Descuento

# Inicialización de variables
total = 0
descuento = 0

# Entrada: número de productos
n = int(input("¿Cuántos productos vas a comprar? "))

# Ciclo para ingresar precios
for i in range(1, n + 1):
    print("Ingrese el precio del producto", i, ": ")
    precio = float(input())

    # Validación del precio
    while precio <= 0:
        print("Precio inválido. Ingresa un valor mayor a 0.")
        print("Ingrese el precio del producto", i, ": ")
        precio = float(input())
    
    total = total + precio

# Aplicación de descuento
if total > 1000:
    descuento = total * 0.10
    total_final = total - descuento
    print("Se aplica un 10% de descuento.")
else:
    total_final = total
    print("No aplica descuento.")

# Salida de resultados
print("-------------------------------")
print("Total sin descuento: $", total)
print("Descuento: $", descuento)
print("Total a pagar: $", total_final)
print("-------------------------------")