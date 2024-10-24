import os
import sqlite3
class BD:
    def __init__(self):
        self.conexion=""
        self.cursor=""

    def conectarBD(self, nombreBD):
        carpeta_base_datos = "base_de_datos"
        if not os.path.exists(carpeta_base_datos):
            os.makedirs(carpeta_base_datos)
        ruta_completa_bd = os.path.join(carpeta_base_datos, nombreBD)
        try:
            print(f"Intentando conectar a la base de datos en: {os.path.abspath(ruta_completa_bd)}")
            self.conexion = sqlite3.connect(ruta_completa_bd)
            self.cursor = self.conexion.cursor()
            print(f"Conexión exitosa a {ruta_completa_bd}")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos {ruta_completa_bd}: {e}")

    def creaBD(self, nombreTabla, campos):
        try:
            campos_str = ', '.join([f'{cn} {cy}' for cn, cy in campos.items() if cn and cy])
            self.cursor.execute(f'CREATE TABLE {nombreTabla} ({campos_str})')
            self.conexion.commit()
            print(f"Tabla '{nombreTabla}' creada exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al crear la tabla '{nombreTabla}':", e)
            print(f'Comando ejecutado: CREATE TABLE {nombreTabla} ({campos_str})')

    def insertarDatos(self,nombreTabla,data):
        try:
            ps2=', '.join(['?' for _ in data])
            self.conexion.execute(F"INSERT INTO {nombreTabla} VALUES ({ps2})", data)
            self.conexion.commit()
        except sqlite3.OperationalError as e:
            return "Error:", e
        
    def imprimirContenido(self, nombreTabla):
        try:
            cursor = self.conexion.execute(f"SELECT * FROM {nombreTabla}")
            filas = cursor.fetchall()
            columnas = [description[0] for description in cursor.description]
            contenido = " | ".join(columnas) + "\n"
            contenido += "-" * (len(contenido) + 5) + "\n"
            for fila in filas:
                contenido += " | ".join(str(item) for item in fila) + "\n"
            return contenido 
        except sqlite3.OperationalError as e:
            return f"Error: {e}"
        
    def obtenerNombresColumnas(self, nombreTabla):
        try:
            self.cursor.execute(f"PRAGMA table_info({nombreTabla});")
            columnas = [info[1] for info in self.cursor.fetchall()]
            return columnas
        except sqlite3.Error as e:
            return e
        
    def obtenerTipoColumnas(self, nombreTabla):
        cursor = self.conexion.cursor()
        cursor.execute(f"PRAGMA table_info({nombreTabla})")
        columnas_info = cursor.fetchall()
        tipos_columnas = {col[1]: col[2] for col in columnas_info}  # Columna: Tipo
        return tipos_columnas


    def cerrarConexion(self):
        if self.conexion:
            self.conexion.close()