'''Implementa una clase Figura, Cuadrado y 
Circulo con su respectiva herencia e implementa los métodos área y 
perímetro haciendo uso de la abtracción y mostrar resultados por consola.'''
#perímetro del cuadrado 4 por el lado
#perímetro del círculo 2 por pi * radio
#área del cuadrado lado al cuadrado
#área del círculo es pi por (radio al cuadrado)

from circulo import Circulo, OtroCirculo
from cuadrado import Cuadrado 


cuadrado1=Cuadrado(3)
circulo1=Circulo(4)
otro_circulo=OtroCirculo(6)

print("Cuadrado")
print(f"El área del cuadrado es {cuadrado1.area()}")
print(f"El perímetro del cuadrado es {cuadrado1.perimetro()}")

print("Círculo")
print(f"El área del circulo es {circulo1.area()}")
print(f"El perímetro del círculo es {circulo1.perimetro()}")
print(f"El otro circulo tiene de perímetro {otro_circulo.perimetro()}")

