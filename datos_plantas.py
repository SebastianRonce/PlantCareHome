from conexion import get_connection

def obtener_datos_plantas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Codigo, Nombre, Temperatura, Riego, TiempoRiego, Recomendacion FROM Plantas")
    filas = cursor.fetchall()
    conn.close()
    return [tuple(fila) for fila in filas]