from figura import Figura
from math import pi as funcion_pi



class Circulo(Figura):
    def __init__(self, radio):
        self.radio=radio

    def area(self):
        return funcion_pi * (self.radio ** 2)
    
    def perimetro(self):
        return 2 * funcion_pi * self.radio
    
class OtroCirculo():
    pi=3,14
    def __init__(self,otro_radio ):
        self.otro_radio=otro_radio
        self.pi=funcion_pi
    def perimetro(self):
        return 2 * funcion_pi * self.otro_radio
         
    

