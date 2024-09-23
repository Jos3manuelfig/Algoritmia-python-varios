class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
        
    def Calcular_area(self):
         return  self.base * self.altura
         
    def Calcular_perimetro(self):
          return 2 * (self.area +self.perimetro)

R1=Rectangulo(5,3)
R1.Calcular_area

print(f'El Area del Rectangulo es: {R1}')
print(f'El Perimetro del Rectangulo es: {R1.Calcular_perimetro}')
 

    