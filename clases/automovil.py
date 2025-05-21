from clases.vehiculo import Vehiculo

class Automovil(Vehiculo):
    ruedas=4;
    def __init__(self,anno,modelo,color, marca, aceleracion,velocidad):
        super().__init__(anno,modelo)
        self.color=color
        self.marca=marca
        self.aceleracion=aceleracion
        self.velocidad=velocidad
        self.__nro_chasis=159556656
    def acelera(self):
       self.velocidad=self.velocidad+self.aceleracion
    def frena(self):
       self.velocidad=self.velocidad-self.aceleracion
       if(self.velocidad<0):
          self.velocidad=0
    def conducir(self):
      return "Conduciendo un automovil"
    def datos(self):
       return f"Soy un automovil de {self.ruedas} ruedas"

#coche=Automovil("amarillo", "Toyota",10,10)

'''print(f"el coche de {coche.ruedas} ruedas tiene una aceleración de {coche.aceleracion}")
print("++++++++++++++++++++++++")
coche.frena()
print(f"velocidad de {coche.velocidad}")
coche.frena()
print(f"velocidad 2 de {coche.velocidad}")
coche.acelera()
print(f"velocidad 3 de {coche.velocidad}")
coche.velocidad=20
coche.aceleracion=20
print(f"velocidad 4 de {coche.velocidad}")
coche.acelera()
print(f"velocidad 5 de {coche.velocidad}")'''

 
