class Rectangulo:
    def  __init__ (self, ancho, alto):
        self.ancho = ancho
        self.alto= alto
        
    def Area(self):
        resul= self.ancho *self.alto
        return resul
        
        
        
    def Perimetro(self):
            resul= 2 * (self.ancho +self.alto)
            return resul
            
            
            
r= Rectangulo(4,2)


print(f'El Area es: {r.Area()}')
print(f'El perimetro es: {r.Perimetro()}')