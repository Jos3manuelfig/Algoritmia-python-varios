class Cafe:
    def descripcion(self):
        return 'café básico'
    
    def costo(self):
        return 1.00  # Costo base corregido a 1.00
        
class DecoradorCafe(Cafe):
    def __init__(self, cafe: Cafe):
        self.cafe = cafe
        
    def descripcion(self):
        return self.cafe.descripcion()
         
    def costo(self):
        return self.cafe.costo()
                 
class Leche(DecoradorCafe):
    def descripcion(self):
        return f"{self.cafe.descripcion()} con leche"

    def costo(self):
        return self.cafe.costo() + 1.50  # Costo de la leche corregido a 1.50

class Azucar(DecoradorCafe):
    def descripcion(self):
        return f"{self.cafe.descripcion()} con azúcar"

    def costo(self):
        return self.cafe.costo() + 0.90  # Costo del azúcar corregido a 0.90
             
# Crear el café básico
cafe = Cafe()
print(cafe.descripcion())  # café básico
print(cafe.costo())        # 1.00

# Decorar el café con leche
cafe_con_leche = Leche(cafe)
print(cafe_con_leche.descripcion())  # café básico con leche
print(cafe_con_leche.costo())        # 2.50 (1.00 + 1.50)

# Decorar el café con leche con azúcar
cafe_con_leche_y_azucar = Azucar(cafe_con_leche)
print(cafe_con_leche_y_azucar.descripcion())  # café básico con leche con azúcar
print(cafe_con_leche_y_azucar.costo())        # 3.40 (2.50 + 0.90)

cafeloco=Azucar(Leche(Azucar(Leche(cafe))))
print(cafeloco.descripcion())
print(cafeloco.costo())