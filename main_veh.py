from clases.automovil import Automovil
from clases.automovilVolador import AutomovilVolador



auto1=Automovil(2020,"Yaris","amarillo", "Toyota",10,10)

print(auto1.color)
print(auto1._Automovil__nro_chasis)
print(f"Año {auto1.get_anno()}")
auto1.set_anno(1990)
print(f"Año {auto1.get_anno()}")
auto1.__modelo="Corola"
auto1.set_modelo("Corolaaaaaaa")
print(f"Año {auto1.get_modelo()}")

#auto2=AutomovilVolador("verde","Ford",10,10)

#print(auto2.marca)
