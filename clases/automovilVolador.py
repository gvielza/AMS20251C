from clases.vehiculo import Vehiculo

class AutomovilVolador(Vehiculo):
   ruedas=6
   def __init__(self,anno,modelo, color, marca, aceleracion, velocidad):
      super().__init__(anno,modelo)
      self.color=color
      self.marca=marca
      self.aceleracion=aceleracion
      self.velocidad=velocidad 
      esta_volando=True
   def conducir(self):
      return "conduciendo automovil Volador"
   def datos(self):
       return f"Soy un automovil volador de {self.ruedas} ruedas"
      
#autom_Volador=AutomovilVolador("verde","Ford",10,10,False)


   
#print(f"El automovil volador tiene {autom_Volador.ruedas}")



'''auto=Automovil("amarillo", "Toyota",10,10)
autom_Volador2=AutomovilVolador("verde","Ford",10,10,False)

print(auto.conducir()) 
print(autom_Volador2.conducir()) '''