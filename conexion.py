import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-J1HDIU5\\SQLEXPRESS;"    # ej: localhost o DESKTOP-XXX\SQLEXPRESS
        "DATABASE=PlantCareHome;"
        "UID=sa;"
        "PWD=T1o2b3i4;"
        # Si usas autenticación de Windows en vez de usuario/contraseña:
        # "Trusted_Connection=yes;"
    )
    return conn