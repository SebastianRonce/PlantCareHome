import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-J1HDIU5\\SQLEXPRESS;"    
        "DATABASE=PlantCareHome;"
        "UID=sa;"
        "PWD=T1o2b3i4;"
    )
    return conn