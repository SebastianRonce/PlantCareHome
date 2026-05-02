from conexion import get_connection

def agregar_planta(nombre, temperatura, riego, tiempo_riego, recomendacion):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Plantas (Nombre, Temperatura, Riego, TiempoRiego, Recomendacion)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, temperatura, riego, tiempo_riego, recomendacion))
    conn.commit()
    conn.close()
    print("✓ Planta agregada exitosamente.")

def editar_planta(codigo, nombre, temperatura, riego, tiempo_riego, recomendacion):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Plantas
        SET Nombre=?, Temperatura=?, Riego=?, TiempoRiego=?, Recomendacion=?
        WHERE Codigo=?
    """, (nombre, temperatura, riego, tiempo_riego, recomendacion, codigo))
    conn.commit()
    conn.close()
    print("✓ Planta actualizada exitosamente.")

def eliminar_planta(codigo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Plantas WHERE Codigo=?", (codigo,))
    conn.commit()
    conn.close()
    print("✓ Planta eliminada exitosamente.")