#   PROGRAMA PARA CONTROL DE INVENTARIO Y VENTAS

import time     # para la espera del mensaje de bienvenida
import csv      # para guardar y leer archivos CSV
from datetime import datetime 

# Archivos donde se guarda todo
archivo_productos = "productos.csv"
archivo_ventas = "ventas.csv"
archivo_salidas = "salidas.csv"
archivo_sistema = "reporte_sistema.txt


def main():
    """
    Aquí va el flujo principal:
    - pedir nombre
    - mensaje de bienvenida con 5 segundos
    - cargar productos desde CSV
    - mostrar menú en un ciclo
    """
    nombre = solicitar_nombre()
    mensaje_bienvenida(nombre)

inventario = cargar_productos_csv()

while True:
    opcion = mostrar_menu_principal()

if opcion == "1":
    agregar_producto(inventario)

elif opcion == "2":
    mostrar_productos(inventario)

elif opcion == "3":
    buscar_producto(inventario)

elif opcion == "4":
    menu_ventas(inventario)

elif opcion == "5":
    salida_manual(inventario)

elif opcion == "6":
    reporte_ventas()

elif opcion == "7":
    if cerrar_programa():
        break

elif opcion == "8":
    reporte_salidas()}

else:
    print("Opcion invalida")


def solicitar_nombre():
    """
    Pide el nombre del usuario y lo regresa.
    """
    return input("Ingresa tu nombre:")


def mensaje_bienvenida(nombre):
   print(f"\nBienvenido{nombre},cargando el sistema...")


def mostrar_menu_principal():

    print(".....Menu principal.....")
    print("1. Agregar un producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Venta")
    print("5. Salida manual")
    print("6. Reporte de ventas")
    print("7. Cerrar programa")
    print("8. Reporte de salidas")
    return input("Elige opción: ")
    


def capturar_fecha():
# forma 1:
    from datetime import date, datetime

# Solo la fecha (día, mes, año)
hoy = date.today()
print("Fecha de hoy:", hoy
    """
#    Pide la fecha (dd/mm/aaaa) y la regresa como tupla.

    """
    # validar formato y convertir a tupla
    ...


def cargar_productos_csv():
   inventario = {}

    try:
        with open(archivo_productos, "r") as file:
            lector = csv.reader(file)
            for nombre, precio, cantidad in lector:
                inventario[nombre] = {
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                }
    except FileNotFoundError:
       
        pass

    return inventario

def guardar_productos_csv(inventario):
    """
    Guarda inventario en productos.csv.
    """
    with open(archivo_productos, "w", newline="") as file:
        escritor = csv.writer(file)
        for nombre, datos in inventario.items():
            escritor.writerow([nombre, datos["precio"], datos["cantidad"]])

   


def agregar_producto(inventario):
    
    nombre = input("Nombre del producto: ").lower()
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    if nombre in inventario:
        inventario[nombre]["cantidad"] += cantidad
    else:
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}

    guardar_productos_csv(inventario)
    print("Producto agregado correctamente.")


def mostrar_productos(inventario):
    print("\n--- INVENTARIO ---")
    if not inventario:
        print("No hay productos.")
        return

    for nombre, datos in inventario.items():
        print(f"{nombre} | Precio: {datos['precio']} | Cantidad: {datos['cantidad']}")



def buscar_producto(inventario):
     p = input("¿Qué producto buscas? ").lower()
    if p in inventario:
        datos = inventario[p]
        print(f"{p}: Precio {datos['precio']}, Cantidad {datos['cantidad']}")
    else:
        print("Ese producto no existe.")


def menu_ventas(inventario):
     """
    Lógica de ventas. Usa fecha actual automáticamente.
    """
    producto = input("Producto: ").lower()

    if producto not in inventario:
        print("No existe ese producto.")
        return

    cantidad = int(input("Cantidad a vender: "))

    if cantidad > inventario[producto]["cantidad"]:
        print("No hay suficientes existencias.")
        return

    precio = inventario[producto]["precio"]
    subtotal = precio * cantidad

    if cantidad >= 10:
        descuento = subtotal * 0.10
    else:
        descuento = 0

    total = subtotal - descuento

    # Reducir existencias
    inventario[producto]["cantidad"] -= cantidad
    guardar_productos_csv(inventario)

    # Obtener fecha actual automáticamente
    ahora = datetime.now()
    fecha_str = f"{ahora.day:02d}/{ahora.month:02d}/{ahora.year}"

    guardar_venta_csv(fecha_str, producto, cantidad, precio, subtotal, descuento, total)

    print(f"Venta realizada. Total: ${total:.2f}")


def guardar_venta_csv(fecha, producto, cantidad, precio, subtotal, descuento, total):
    """
    Guarda una venta nueva en ventas.csv.
    """
    # abrir CSV en modo append y escribir la venta
    ...


def salida_manual(inventario):
   """
    Registra una salida manual. Fecha actual automáticamente.
    """
    producto = input("Producto: ").lower()

    if producto not in inventario:
        print("No existe ese producto.")
        return

    cantidad = int(input("Cantidad a sacar: "))

    if cantidad > inventario[producto]["cantidad"]:
        print("Cantidad insuficiente.")
        return

    # Reducir existencias
    inventario[producto]["cantidad"] -= cantidad
    guardar_productos_csv(inventario)

    # Fecha actual
    ahora = datetime.now()
    fecha_str = f"{ahora.day:02d}/{ahora.month:02d}/{ahora.year}"

def guardar_salida_csv(fecha, producto, cantidad):
    """
    Guarda una salida manual en el archivo salidas.csv.
    """
    # write en CSV
    ...


def reporte_ventas():
  print("\n ------REPORTE DE VENTAS-----")
    try:
         with open(archivo_ventas,newline='',encoding='utf-8') as f:
         lector = csv.reader(f)
         for line in lector:
         print(linea)
    except FileNotFoundError:
    print("no hay ventas registradas")
    
    # leer CSV y filtrar según lo que el usuario pida
    ...


def reporte_salidas():
    """
    Permite ver salidas:
    - por día
    - por mes
    - por año
    leyendo salidas.csv
    """
    # leer CSV y mostrar según filtro
    ...


def cerrar_programa():
    """
    Pregunta si se quiere cerrar.
    si = muestra 'gracias por usar el programa puto'
    no = regresa al menú
    """
    # input(), decisión del usuario
    ...

    main()

#vamos equipo #fuerzaleona 

#si se puede 










