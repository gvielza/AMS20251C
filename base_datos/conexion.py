import sqlite3

class Conexion:
    def __init__(self, path_bd):
        self.conexion=sqlite3.connect(path_bd)
        self.cursor=self.conexion.cursor()
        self.crear_tabla_usuario()


    def crea_tabla_usuario(self):
        