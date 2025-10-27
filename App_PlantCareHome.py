# Importar los datos de plantas desde el archivo externo
from datos_plantas import obtener_datos_plantas

class planta:
    def __init__(self, codigo: int, nombre: str, temperatura: str, riego: str, tiempo_riego: str, altura: str, recomendacion: str):
        self.codigo = codigo
        self.nombre = nombre
        self.temperatura = temperatura
        self.riego = riego
        self.tiempo_riego = tiempo_riego
        self.altura = altura
        self.recomendacion = recomendacion

    def mostrar_planta(self):
        print("-----------------------------------------------------------------------------------------------")
        print(f"Codigo = {self.codigo}")
        print(f"Nombre = {self.nombre}")
        print(f"Temperatura = {self.temperatura}")
        print(f"Riego = {self.riego}")
        print(f"Tiempo de riego = {self.tiempo_riego}")
        print(f"Altura = {self.altura}")
        print(f"Recomendacion = {self.recomendacion}")
        print("----------------------------------------------------------------------------------------------")
        
plantas: list[planta] = []
favoritos: list[planta] = []

def cargar_plantas():
    """Carga las plantas desde el archivo de datos externo"""
    datos = obtener_datos_plantas()
    for datos_planta in datos:
        codigo, nombre, temperatura, riego, tiempo_riego, altura, recomendacion = datos_planta
        plantas.append(planta(codigo, nombre, temperatura, riego, tiempo_riego, altura, recomendacion))

def buscar_por_nombre(nombre: str):
    for planta in plantas:
        if planta.nombre == nombre:
            planta.mostrar_planta()
            return planta
    print("La planta no se encuentra en la base de datos ")
    return None

def buscar_por_codigo(codigo: int):
    for planta in plantas:
        if planta.codigo == codigo:
            planta.mostrar_planta()
            return planta
    print("La planta no se encuentra en la base de datos ")
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
    for planta in favoritos:
        planta.mostrar_planta()

def validar_numero(mensaje):
    cantidad = input(mensaje)
    if not cantidad.isnumeric():
        print("ERROR!")
        print("--------------------\n")
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
    for i, planta in enumerate(plantas, 1):
        print(f"\n{'-'*80}")
        print(f"Planta #{i}")
        planta.mostrar_planta()
    
    print("\nSelecciona una planta para agregar a favoritos")
    numero_planta = validar_numero(f"\nEscribe el número de la planta (1-{len(plantas)}) o 0 para cancelar: ")
    
    if 1 <= numero_planta <= len(plantas):
        planta_seleccionada = plantas[numero_planta - 1]
        agregar_favorito(planta_seleccionada)
    elif numero_planta == 0:
        return
    else:
        print("\nNúmero de planta inválido.")

def favoritos_menu():
    if not favoritos:
        print("\nNo tienes plantas en favoritos.")
        return
    
    print("\n=== MIS FAVORITOS ===")
    mostrar_favoritos()
    
    print("\n1. Eliminar una planta de favoritos")
    print("2. Volver al menú principal")
    
    opcion = validar_numero("\nSelecciona una opción (1-2): ")
    
    if opcion == 1:
        print("\nSelecciona la planta a eliminar:")
        for i, planta in enumerate(favoritos, 1):
            print(f"{i}. {planta.nombre}")
        
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


# Cargar las plantas desde el archivo de datos y ejecutar el programa
cargar_plantas()
inventario()