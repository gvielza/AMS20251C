class Calculadora():

    def sumar(self,a,b):
        return a + b
    
    def restar(self,r,s):
        return r - s
    
    def multiplicar(self, a,b):
        return a*b
    
    def dividir(self, a,b):
        if b==0:
            raise ValueError("No se puede dividir por 0")
        return a/b
    


