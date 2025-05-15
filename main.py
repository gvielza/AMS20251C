'''Implementa una clase Figura, Cuadrado y 
Circulo con su respectiva herencia e implementa los métodos área y 
perímetro haciendo uso de la abtracción y mostrar resultados por consola.'''

from cuadrado import Cuadrado
from circulo import Circulo

cuadrado1=Cuadrado(3)
circulo1=Circulo(4)

print("Cuadrado")
print(f"El área del cuadrado es {cuadrado1.area()}")

print("Círculo")
print(f"El área del circulo es {circulo1.area()}")

