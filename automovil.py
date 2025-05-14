from abc import ABC, abstractmethod

class Vehiculo(ABC):   
   @abstractmethod
   def conducir(self):
      pass

class Automovil(Vehiculo):
    ruedas=4;
    def __init__(self,color, marca, aceleracion,velocidad):
        self.color=color
        self.marca=marca
        self.aceleracion=aceleracion
        self.velocidad=velocidad
    def acelera(self):
       self.velocidad=self.velocidad+self.aceleracion
    def frena(self):
       self.velocidad=self.velocidad-self.aceleracion
       if(self.velocidad<0):
          self.velocidad=0
    def conducir(self):
      return "Conduciendo un automovil"

coche=Automovil("amarillo", "Toyota",10,10)

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

class AutomovilVolador(Automovil):
   ruedas=6
   def __init__(self, color, marca, aceleracion, velocidad,esta_volando=True):
      super().__init__(color, marca, aceleracion, velocidad)
   def conducir(self):
      return "conduciendo automovil Volador"
      
autom_Volador=AutomovilVolador("verde","Ford",10,10,False)


   
print(f"El automovil volador tiene {autom_Volador.ruedas}")



auto=Automovil("amarillo", "Toyota",10,10)
autom_Volador2=AutomovilVolador("verde","Ford",10,10,False)

print(auto.conducir()) 
print(autom_Volador2.conducir())  
