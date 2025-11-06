import os
import time
import pymysql

host = os.getenv("MYSQL_HOST", "db")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")

print("Esperando que MySQL esté listo...")

while True:
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            connect_timeout=5
        )
        conn.close()
        print("MySQL listo.")
        break
    except Exception:
        print("No disponible aún, reintentando en 2s...")
        time.sleep(2)
