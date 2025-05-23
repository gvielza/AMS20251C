from base_datos.conexion import Conexion

mi_conexion=Conexion()

#mi_conexion.insertar_usuario("Gionnelly","gvielza","gionnelly.vielza@davinci.edu.ar","user")


users=mi_conexion.mostrar_usuarios()
#mi_conexion.eliminar_usuario(4)

for usuario in users:
    print(usuario)