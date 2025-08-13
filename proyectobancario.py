# Sistema Gestion de Cuentas Bancarias

# Crear Funciones de registro de clientes con datos
# Crear Funcion para depositar dinero (asociar un saldo a cliente)
# Crear Funcion para retirar dinero (asociar un saldo a cliente)
# Crear funcion para consultar un prestamo de los distintos asociados a una cuenta, pidiendo CC y seleccionando de la lista visible,
# De este prestamo mostrar fecha de inicio del prestamo, si esta activo, inactivo, cancelado o pagado, tambien cuanto de este esta pago y cuanto falta.

# Crear Funcion de prestamo y pago de cuota a este
# Crear funcion para eliminar cliente 

## Funciones Menu
# 1. Crear Cuenta
# 2. Depositar Dinero
# 3. Solicitar Credito
# 4. Consultar Credito
# 5. Retirar Dinero
# 6. Pago Cuota Credito
# 7. Cancelar Cuenta
# 8. Salir

## Datos Cliente
# CC
# Nombre
# Email
# Edad
# Contacto > movil, fijo
# Ubicacion > pais, dep, ciudad

clientes = {}

def registrar_cliente(CC):
    if CC not in clientes:
        nombre = input("Ingrese el Nombre del Cliente: ")
        email = input("Ingrese el Correo Electronico del Cliente: ")
        edad = int(input("Ingrese la Edad del Cliente: "))
        saldo = float(input("Ingrese el saldo inicial del Cliente:"))
        movil = input("Ingrese el nº de Telefono del Cliente: ")
        fijo = input ("Ingrese el # de Telefono Fijo del Cliente: ")
        pais = input("Ingrese el pais de residencia del Cliente: ")
        dep = input("Ingrese el Departamento de residencia del Cliente: ")
        ciudad = input("Ingrese la Ciudad de residencia del Cliente: ")

        clientes[CC] = {"nombre":nombre, "email":email, "edad":edad, "saldo": saldo, "contacto": {"movil":movil, "fijo":fijo}, "ubicacion": {"pais":pais, "dep":dep, "ciudad":ciudad}}
        print (f"El Cliente con CC {CC} se ha registrado exitosamente!")
    else:
        print (f"El cliente con el numero de identificacion {CC} ya se encuentra registrado.")

def registrar_dato():
    CC = input("Ingrese el numero de identificacion del cliente: ")
    if CC in clientes:

def depositar_dinero(CC):
    if CC in clientes:




# Diseño Menu Principal

menuPrincipal = "Menu Principal\n1. Crear Cuenta\n2. Depositar Dinero\n3. Solicitar Credito\n4. Consultar Credito\n5. Retirar Dinero\n6. Pago Cuota Credito\n7. Cancelar Cuenta\n8. Salir"

opcionMenu = input(menuPrincipal)
match opcionMenu:
    case "1":
        while True:
            CC = input("Ingrese la Cedula de Ciudadania: ")
            registrar_cliente(CC)
            # Crear Cuenta
    case "2":
        while True:

            # Depositar Dinero
    case "3":
        while True:
            # Solicitar Credito
    case "4":
        while True:
            # Consultar Credito
    case "5":
        while True:
            # Retirar Dinero
    case "6":
        while True:
            # Pago Cuota Credito
    case "7":
        while True:
            # Cancelar Cuenta
    case "8":
        break
            # Salir 
 
        



