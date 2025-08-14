# Sistema Gestión de Cuentas Bancarias Simple
import os

# Diccionarios para almacenar los datos
clientes = {}
prestamos = {}

def limpiar_pantalla():
    """Limpia la pantalla"""
    os.system('clear' if os.name == 'posix' else 'cls')

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n=== SISTEMA BANCARIO ===")
    print("1. Crear Cuenta")
    print("2. Depositar Dinero")
    print("3. Solicitar Credito")
    print("4. Consultar Credito")
    print("5. Retirar Dinero")
    print("6. Pago Cuota Credito")
    print("7. Cancelar Cuenta")
    print("8. Salir")
    print("========================")

def registrar_cliente():
    """Registra un nuevo cliente"""
    cc = input("Ingrese la Cedula de Ciudadania: ")
    
    if cc in clientes:
        print(f"El cliente con CC {cc} ya se encuentra registrado.")
        return
    
    print("--- Datos del Cliente ---")
    nombre = input("Ingrese el Nombre del Cliente: ")
    email = input("Ingrese el Correo Electronico del Cliente: ")
    edad = int(input("Ingrese la Edad del Cliente: "))
    saldo = float(input("Ingrese el saldo inicial del Cliente: "))
    movil = input("Ingrese el numero de Telefono del Cliente: ")
    fijo = input("Ingrese el # de Telefono Fijo del Cliente: ")
    pais = input("Ingrese el pais de residencia del Cliente: ")
    dep = input("Ingrese el Departamento de residencia del Cliente: ")
    ciudad = input("Ingrese la Ciudad de residencia del Cliente: ")
    
    clientes[cc] = {
        "nombre": nombre,
        "email": email,
        "edad": edad,
        "saldo": saldo,
        "contacto": {"movil": movil, "fijo": fijo},
        "ubicacion": {"pais": pais, "dep": dep, "ciudad": ciudad},
        "activa": True
    }
    
    print(f"El Cliente {nombre} con CC {cc} se ha registrado exitosamente!")

def depositar_dinero():
    """Deposita dinero a una cuenta"""
    cc = input("Ingrese la CC del cliente: ")
    
    if cc not in clientes:
        print("Cliente no encontrado.")
        return
    
    if not clientes[cc]["activa"]:
        print("La cuenta esta cancelada.")
        return
    
    monto = float(input("Ingrese el monto a depositar: "))
    
    if monto <= 0:
        print("El monto debe ser mayor a cero.")
        return
    
    clientes[cc]["saldo"] += monto
    print(f"Deposito exitoso! Nuevo saldo: ${clientes[cc]['saldo']:,.2f}")

def retirar_dinero():
    """Retira dinero de una cuenta"""
    cc = input("Ingrese la CC del cliente: ")
    
    if cc not in clientes:
        print("Cliente no encontrado.")
        return
    
    if not clientes[cc]["activa"]:
        print("La cuenta esta cancelada.")
        return
    
    monto = float(input("Ingrese el monto a retirar: "))
    
    if monto <= 0:
        print("El monto debe ser mayor a cero.")
        return
    
    if monto > clientes[cc]["saldo"]:
        print("Saldo insuficiente.")
        print(f"Saldo disponible: ${clientes[cc]['saldo']:,.2f}")
        return
    
    clientes[cc]["saldo"] -= monto
    print(f"Retiro exitoso! Nuevo saldo: ${clientes[cc]['saldo']:,.2f}")

def solicitar_credito():
    """Solicita un credito"""
    cc = input("Ingrese la CC del cliente: ")
    
    if cc not in clientes:
        print("Cliente no encontrado.")
        return
    
    if not clientes[cc]["activa"]:
        print("La cuenta esta cancelada.")
        return
    
    print("--- Tipos de Credito ---")
    print("1. Personal")
    print("2. Vehicular") 
    print("3. Hipotecario")
    
    tipo = input("Seleccione tipo de credito (1-3): ")
    tipos = {"1": "Personal", "2": "Vehicular", "3": "Hipotecario"}
    
    if tipo not in tipos:
        print("Tipo de credito invalido.")
        return
    
    monto = float(input("Ingrese el monto del credito: "))
    cuotas = int(input("Ingrese el numero de cuotas: "))
    
    if monto <= 0 or cuotas <= 0:
        print("Monto y cuotas deben ser mayores a cero.")
        return
    
    # Calcular cuota mensual simple
    cuota_mensual = monto / cuotas
    
    # Crear ID simple para el prestamo
    id_prestamo = f"{cc}-{len(prestamos) + 1}"
    
    prestamos[id_prestamo] = {
        "cc_cliente": cc,
        "tipo": tipos[tipo],
        "monto_original": monto,
        "monto_pendiente": monto,
        "cuotas_totales": cuotas,
        "cuotas_pagadas": 0,
        "cuota_mensual": cuota_mensual,
        "estado": "activo"
    }
    
    # Depositar dinero en la cuenta
    clientes[cc]["saldo"] += monto
    
    print(f"Credito aprobado!")
    print(f"ID Prestamo: {id_prestamo}")
    print(f"Tipo: {tipos[tipo]}")
    print(f"Monto: ${monto:,.2f}")
    print(f"Cuotas: {cuotas}")
    print(f"Cuota mensual: ${cuota_mensual:,.2f}")

def consultar_credito():
    """Consulta los creditos de un cliente"""
    cc = input("Ingrese la CC del cliente: ")
    
    if cc not in clientes:
        print("Cliente no encontrado.")
        return
    
    # Buscar prestamos del cliente
    prestamos_cliente = []
    for id_prestamo, prestamo in prestamos.items():
        if prestamo["cc_cliente"] == cc:
            prestamos_cliente.append((id_prestamo, prestamo))
    
    if not prestamos_cliente:
        print("No se encontraron creditos para este cliente.")
        return
    
    print(f"\n--- Creditos de {clientes[cc]['nombre']} ---")
    print(f"CC: {cc}")
    print("-" * 50)
    
    for i, (id_prestamo, prestamo) in enumerate(prestamos_cliente, 1):
        print(f"\n{i}. ID: {id_prestamo}")
        print(f"   Tipo: {prestamo['tipo']}")
        print(f"   Estado: {prestamo['estado'].upper()}")
        print(f"   Monto original: ${prestamo['monto_original']:,.2f}")
        print(f"   Monto pendiente: ${prestamo['monto_pendiente']:,.2f}")
        print(f"   Cuotas pagadas: {prestamo['cuotas_pagadas']}/{prestamo['cuotas_totales']}")
        print(f"   Cuota mensual: ${prestamo['cuota_mensual']:,.2f}")

def pagar_cuota_credito():
    """Paga una cuota de credito"""
    cc = input("Ingrese la CC del cliente: ")
    
    if cc not in clientes:
        print("Cliente no encontrado.")
        return
    
    if not clientes[cc]["activa"]:
        print("La cuenta esta cancelada.")
        return
    
    # Buscar creditos activos del cliente
    creditos_activos = []
    for id_prestamo, prestamo in prestamos.items():
        if prestamo["cc_cliente"] == cc and prestamo["estado"] == "activo":
            creditos_activos.append((id_prestamo, prestamo))
    
    if not creditos_activos:
        print("No tiene creditos activos.")
        return
    
    print("\n--- Creditos Activos ---")
    for i, (id_prestamo, prestamo) in enumerate(creditos_activos, 1):
        print(f"{i}. ID: {id_prestamo} - {prestamo['tipo']}")
        print(f"   Cuota: ${prestamo['cuota_mensual']:,.2f}")
        print(f"   Pendiente: ${prestamo['monto_pendiente']:,.2f}")
    
    seleccion = int(input("Seleccione el credito (numero): ")) - 1
    
    if seleccion < 0 or seleccion >= len(creditos_activos):
        print("Seleccion invalida.")
        return
    
    id_prestamo, prestamo = creditos_activos[seleccion]
    cuota = prestamo["cuota_mensual"]
    
    if clientes[cc]["saldo"] < cuota:
        print(f"Saldo insuficiente.")
        print(f"Saldo disponible: ${clientes[cc]['saldo']:,.2f}")
        print(f"Cuota requerida: ${cuota:,.2f}")
        return
    
    # Procesar pago
    clientes[cc]["saldo"] -= cuota
    prestamos[id_prestamo]["cuotas_pagadas"] += 1
    prestamos[id_prestamo]["monto_pendiente"] -= cuota
    
    # Verificar si el prestamo esta pagado
    if prestamos[id_prestamo]["cuotas_pagadas"] >= prestamos[id_prestamo]["cuotas_totales"]:
        prestamos[id_prestamo]["estado"] = "pagado"
        prestamos[id_prestamo]["monto_pendiente"] = 0
        print("Felicitaciones! Ha pagado completamente su credito.")
    
    print(f"Pago exitoso!")
    print(f"Cuota pagada: ${cuota:,.2f}")
    print(f"Cuotas restantes: {prestamos[id_prestamo]['cuotas_totales'] - prestamos[id_prestamo]['cuotas_pagadas']}")
    print(f"Nuevo saldo: ${clientes[cc]['saldo']:,.2f}")

def cancelar_cuenta():
    """Cancela una cuenta de cliente"""
    cc = input("Ingrese la CC del cliente: ")
    
    if cc not in clientes:
        print("Cliente no encontrado.")
        return
    
    if not clientes[cc]["activa"]:
        print("La cuenta ya esta cancelada.")
        return
    
    # Verificar creditos activos
    creditos_activos = []
    for prestamo in prestamos.values():
        if prestamo["cc_cliente"] == cc and prestamo["estado"] == "activo":
            creditos_activos.append(prestamo)
    
    if creditos_activos:
        print("No puede cancelar la cuenta con creditos activos.")
        print(f"Tiene {len(creditos_activos)} credito(s) pendiente(s).")
        return
    
    print(f"\n--- Informacion de la Cuenta ---")
    print(f"Cliente: {clientes[cc]['nombre']}")
    print(f"CC: {cc}")
    print(f"Saldo actual: ${clientes[cc]['saldo']:,.2f}")
    
    confirmacion = input("\nEsta seguro de cancelar esta cuenta? (si/no): ").lower()
    
    if confirmacion == "si" or confirmacion == "s":
        if clientes[cc]["saldo"] > 0:
            print(f"Se realizara un retiro final de ${clientes[cc]['saldo']:,.2f}")
        
        clientes[cc]["activa"] = False
        print("Cuenta cancelada exitosamente.")
    else:
        print("Cancelacion abortada.")

def main():
    """Funcion principal del sistema"""
    print("Bienvenido al Sistema Bancario")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        
        limpiar_pantalla()
        
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            depositar_dinero()
        elif opcion == "3":
            solicitar_credito()
        elif opcion == "4":
            consultar_credito()
        elif opcion == "5":
            retirar_dinero()
        elif opcion == "6":
            pagar_cuota_credito()
        elif opcion == "7":
            cancelar_cuenta()
        elif opcion == "8":
            print("Gracias por usar nuestro sistema bancario!")
            break
        else:
            print("Opcion invalida. Seleccione del 1 al 8.")
        
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

# Ejecutar el programa
if __name__ == "__main__":
    main()