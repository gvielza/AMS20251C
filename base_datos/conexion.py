import sqlite3

class Conexion:
    def __init__(self, path_bd="base_datos/mi_bd.db"):
        self.conexion=sqlite3.connect(path_bd)
        self.cursor=self.conexion.cursor()
        self.crear_tabla_usuario()


    def crear_tabla_usuario(self):
        self.cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios
               (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT,
               usuario TEXT,
               correo TEXT,
               rol TEXT
               )
''')   
        self.conexion.commit()

    def insertar_usuario(self,nombre, usuario,correo,rol):
        self.cursor.execute('''
               INSERT INTO usuarios (
               nombre,usuario,correo,rol
               )
               VALUES(?, ?, ?, ?)
                ''',(nombre,usuario,correo,rol))
        self.conexion.commit()

    def mostrar_usuarios(self):
        self.cursor.execute("SELECT * from usuarios")
        usuarios=self.cursor.fetchall()
        return usuarios
    
    def eliminar_usuario(self,id):
        self.cursor.execute("DELETE FROM usuarios WHERE id=?",(id,))
        self.conexion.commit()
    
    def cerrar_conexion(self):
        self.conexion.close()