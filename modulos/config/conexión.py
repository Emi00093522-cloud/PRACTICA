import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='beu5uv04siiubuvtnhzp-mysql.services.clever-cloud.com',
            user='usqhvy7ik0yfoilx',
            password='ghEpZtJkPEsx8yL9WiDa',
            database='beu5uv04siiubuvtnhzp',
            port=3306
        )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None

