from clases.automovil import Automovil
from clases.automovilVolador import AutomovilVolador
import sqlite3


auto1=Automovil(2020,"Yaris","amarillo", "Toyota",10,10)

print(auto1.color)
print(auto1._Automovil__nro_chasis)
print(f"Año {auto1.get_anno()}")
auto1.set_anno(1990)
print(f"Año {auto1.get_anno()}")
auto1.__modelo="Corola"
auto1.set_modelo("Corolaaaaaaa")
print(f"Año {auto1.get_modelo()}")

print("**************")

auto2=AutomovilVolador(2024,"FOcus","verde","Ford",10,10)

print(auto2.marca)

def datos(vehiculo):
    return vehiculo.datos()

print(datos(auto2))


print("************BD**************")
conexion=sqlite3.connect("base_datos/mi_bd.db")
cursor=conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS automoviles
               (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               color TEXT,
               marca TEXT,
               aceleracion INTEGER,
               velocidad INTEGER,
               anno INTEGER,
               modelo TEXT
               )
''')

conexion.commit()

vehiculo=Automovil(2025,"Corola","verde","Toyota",10,20)

cursor.execute('''
               INSERT INTO automoviles (
               color,marca,aceleracion,velocidad,anno,modelo
               )
               VALUES(?, ?, ?, ?, ?, ?)
                ''',(vehiculo.color,vehiculo.marca,vehiculo.aceleracion,vehiculo.velocidad,vehiculo.get_anno(),vehiculo.get_modelo()))

conexion.commit()

cursor.execute("SELECT * FROM automoviles")


automoviles=cursor.fetchall()

for fila in automoviles:
    print(fila)




