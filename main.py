# Importar los datos de plantas desde la base de datos
from datos_plantas import obtener_datos_plantas
from crud_plantas import agregar_planta, editar_planta, eliminar_planta

# ─── CLASE ────────────────────────────────────────────────
class planta:
    def __init__(self, codigo: int, nombre: str, 
    temperatura: str, riego: str, tiempo_riego: str, 
    recomendacion: str):

        self.codigo = codigo
        self.nombre = nombre
        self.temperatura = temperatura
        self.riego = riego
        self.tiempo_riego = tiempo_riego
        self.recomendacion = recomendacion

    def mostrar_planta(self):
        print("-----------------------------------------------------------------------------------------------")
        print(f"Codigo = {self.codigo}")
        print(f"Nombre = {self.nombre}")
        print(f"Temperatura = {self.temperatura}")
        print(f"Riego = {self.riego}")
        print(f"Tiempo de riego = {self.tiempo_riego}")
        print(f"Recomendacion = {self.recomendacion}")
        print("----------------------------------------------------------------------------------------------")

# ─── LISTAS ───────────────────────────────────────────────
plantas = []
favoritos = []

# ─── FUNCIONES ORIGINALES ─────────────────────────────────
def cargar_plantas():
    plantas.clear()
    datos = obtener_datos_plantas()
    for datos_planta in datos:
        codigo, nombre, temperatura, riego, tiempo_riego, recomendacion = datos_planta
        plantas.append(planta(codigo, nombre, temperatura, riego, tiempo_riego, recomendacion))

def buscar_por_nombre(nombre: str):
    for p in plantas:
        if p.nombre == nombre:
            p.mostrar_planta()
            return p
    print("La planta no se encuentra en la base de datos.")
    return None

def buscar_por_codigo(codigo: int):
    for p in plantas:
        if p.codigo == codigo:
            p.mostrar_planta()
            return p
    print("La planta no se encuentra en la base de datos.")
    return None

def agregar_favorito(planta_seleccionada):
    if planta_seleccionada and planta_seleccionada not in favoritos:
        favoritos.append(planta_seleccionada)
        print(f"\n✓ '{planta_seleccionada.nombre}' ha sido agregada a favoritos.")
    elif planta_seleccionada and planta_seleccionada in favoritos:
        print(f"\n! '{planta_seleccionada.nombre}' ya está en favoritos.")

def eliminar_favorito(planta_seleccionada):
    if planta_seleccionada and planta_seleccionada in favoritos:
        favoritos.remove(planta_seleccionada)
        print(f"\n✓ '{planta_seleccionada.nombre}' ha sido eliminada de favoritos.")
    else:
        print("\n! La planta no está en favoritos.")

def mostrar_favoritos():
    if not favoritos:
        print("\nNo tienes plantas en favoritos.")
        return
    print("\n========= MIS FAVORITOS =========")
    for p in favoritos:
        p.mostrar_planta()

def validar_numero(mensaje):
    cantidad = input(mensaje)
    if not cantidad.isnumeric():
        print("ERROR! Ingresa un número válido.")
        return validar_numero(mensaje)
    return int(cantidad)

def mostrar_menu_principal():
    print("\n" + "="*80)
    print("                   ¡Bienvenido a PlantCareHome!")
    print("="*80)
    print("\n1. Buscar planta")
    print("2. Mostrar todas las plantas")
    print("3. Mis favoritos")
    print("4. Salir")
    print()

def buscar_planta_menu():
    print("\n=== BUSCAR PLANTA ===")
    print("1. Buscar por código")
    print("2. Buscar por nombre")
    print("3. Volver al menú principal")
    
    opcion_buscar = validar_numero("\nSelecciona una opción (1-3): ")
    
    if opcion_buscar == 1:
        codigo = validar_numero("\nEscribe el código de la planta: ")
        planta_encontrada = buscar_por_codigo(codigo)
        if planta_encontrada:
            opcion_favorito = input("\n¿Deseas agregar esta planta a favoritos? (s/n): ").lower()
            if opcion_favorito == 's':
                agregar_favorito(planta_encontrada)
    elif opcion_buscar == 2:
        nombre = input("\nEscribe el nombre de la planta: ")
        planta_encontrada = buscar_por_nombre(nombre)
        if planta_encontrada:
            opcion_favorito = input("\n¿Deseas agregar esta planta a favoritos? (s/n): ").lower()
            if opcion_favorito == 's':
                agregar_favorito(planta_encontrada)
    elif opcion_buscar == 3:
        return
    else:
        print("Opción incorrecta.")
        buscar_planta_menu()

def mostrar_todas_las_plantas():
    if not plantas:
        print("\nNo hay plantas disponibles.")
        return
    print("\n=== LISTA DE PLANTAS ===")
    for i, p in enumerate(plantas, 1):
        print(f"\n{'-'*80}")
        print(f"Planta #{i}")
        p.mostrar_planta()
    
    print("\nSelecciona una planta para agregar a favoritos")
    numero_planta = validar_numero(f"\nEscribe el número de la planta (1-{len(plantas)}) o 0 para cancelar: ")
    
    if 1 <= numero_planta <= len(plantas):
        agregar_favorito(plantas[numero_planta - 1])
    elif numero_planta == 0:
        return
    else:
        print("\nNúmero de planta inválido.")

def favoritos_menu():
    if not favoritos:
        print("\nNo tienes plantas en favoritos.")
        return
    mostrar_favoritos()
    print("\n1. Eliminar una planta de favoritos")
    print("2. Volver al menú principal")
    
    opcion = validar_numero("\nSelecciona una opción (1-2): ")
    
    if opcion == 1:
        print("\nSelecciona la planta a eliminar:")
        for i, p in enumerate(favoritos, 1):
            print(f"{i}. {p.nombre}")
        numero_planta = validar_numero(f"\nEscribe el número de la planta (1-{len(favoritos)}): ")
        if 1 <= numero_planta <= len(favoritos):
            eliminar_favorito(favoritos[numero_planta - 1])
        else:
            print("\nNúmero inválido.")

def inventario():
    while True:
        mostrar_menu_principal()
        opcion = validar_numero("Selecciona una opción (1-4): ")
        
        if opcion == 1:
            buscar_planta_menu()
        elif opcion == 2:
            mostrar_todas_las_plantas()
        elif opcion == 3:
            favoritos_menu()
        elif opcion == 4:
            print("\n¡Gracias por usar PlantCareHome!")
            break
        else:
            print("\nOpción incorrecta. Por favor selecciona una opción válida.")

# ─── LOGIN ────────────────────────────────────────────────
USUARIOS = {
    "admin": {"password": "admin123", "rol": "admin"},
    "usuario": {"password": "12345",   "rol": "usuario"},
}

def login():
    print("\n" + "="*80)
    print("              Bienvenido a PlantCareHome")
    print("="*80)
    user = input("Usuario: ").strip()
    pwd  = input("Contraseña: ").strip()
    if user in USUARIOS and USUARIOS[user]["password"] == pwd:
        print(f"\n✓ Bienvenido, {user}!")
        return USUARIOS[user]["rol"]
    print("\n✗ Usuario o contraseña incorrectos.")
    return login()

# ─── MENÚ ADMIN ───────────────────────────────────────────
def pedir_datos_planta():
    nombre        = input("Nombre: ")
    temperatura   = input("Temperatura: ")
    riego         = input("Riego: ")
    tiempo_riego  = input("Tiempo de riego: ")
    recomendacion = input("Recomendación: ")
    return nombre, temperatura, riego, tiempo_riego, recomendacion

def menu_admin():
    while True:
        print("\n" + "="*80)
        print("                     PANEL DE ADMINISTRADOR")
        print("="*80)
        print("1. Agregar planta")
        print("2. Editar planta")
        print("3. Eliminar planta")
        print("4. Ver todas las plantas")
        print("5. Salir")

        opcion = validar_numero("Selecciona una opción (1-5): ")

        if opcion == 1:
            print("\n=== AGREGAR PLANTA ===")
            datos = pedir_datos_planta()
            agregar_planta(*datos)
            cargar_plantas()

        elif opcion == 2:
            print("\n=== EDITAR PLANTA ===")
            codigo = validar_numero("Código de la planta a editar: ")
            print("Ingresa los nuevos datos:")
            datos = pedir_datos_planta()
            editar_planta(codigo, *datos)
            cargar_plantas()

        elif opcion == 3:
            print("\n=== ELIMINAR PLANTA ===")
            codigo = validar_numero("Código de la planta a eliminar: ")
            confirmar = input(f"¿Seguro que deseas eliminar la planta {codigo}? (s/n): ").lower()
            if confirmar == 's':
                eliminar_planta(codigo)
                cargar_plantas()

        elif opcion == 4:
            mostrar_todas_las_plantas()

        elif opcion == 5:
            print("\n¡Hasta luego!")
            break

# ─── EJECUCIÓN ────────────────────────────────────────────
cargar_plantas()
rol = login()

if rol == "admin":
    menu_admin()
else:
    inventario()