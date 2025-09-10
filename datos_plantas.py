# Archivo de datos de plantas para Plantify
# Este archivo contiene la información de todas las plantas disponibles

def obtener_datos_plantas():
    """
    Retorna una lista con los datos de todas las plantas.
    Cada elemento es una tupla con los datos de una planta en el orden:
    (codigo, nombre, temperatura, riego, tiempo_riego, altura, recomendacion)
    """
    datos_plantas = [
        (1, "Sabila", "20° a 25°C.", "Una cada 10 o 14 dias.", "Durante 3 minutos.", "20 a 25 Cm.", 
         """ La sabila necesita suelos ricos en materia orgánica
y con buen drenaje que eviten los encharcamientos. """),
        
        (2, "Cilantro", "10° a 24°C.", "2 o 3 veces por semana.", "Durante 3 minutos.", "40 a 70 Cm.", 
         """ El cilantro necesita nitrógeno, fósforo y potasio para crecer de manera óptima.
Además de los nutrientes básicos, también requiere calcio, magnesio y azufre."""),
        
        (3, "Calathea", "18° a 24°C.", "1 o 2 veces por semnana.", "Metodo de inversión por 15 minutos.", "12 Cm.", 
         """Las Calathea necesita un suelo húmedo, con buena luz pero no directa al sol
 y buena tierra con mezclas vegetales. """)
    ]
    
    return datos_plantas
