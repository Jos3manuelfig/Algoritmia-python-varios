from abc import ABC, abstractmethod

# Clase abstracta para definir la interfaz de un café
class Cafe(ABC):
    
    @abstractmethod
    def descripcion(self):
        pass
    
    @abstractmethod
    def costo(self):
        pass

# Implementación concreta del café básico
class CafeBasico(Cafe):
    def descripcion(self):
        return 'café básico'
    
    def costo(self):
        return 1.00  # Costo base de 1.00

# Clase abstracta decoradora que también hereda de Cafe
class DecoradorCafe(Cafe):
    
    def __init__(self, cafe: Cafe):
        self.cafe = cafe

    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def costo(self):
        pass

# Decorador de Leche
class Leche(DecoradorCafe):
    
    def descripcion(self):
        return f"{self.cafe.descripcion()} con leche"

    def costo(self):
        return self.cafe.costo() + 1.50  # Costo de la leche de 1.50

# Decorador de Azúcar
class Azucar(DecoradorCafe):
    
    def descripcion(self):
        return f"{self.cafe.descripcion()} con azúcar"

    def costo(self):
        return self.cafe.costo() + 0.90  # Costo del azúcar de 0.90

# Crear el café básico
cafe = CafeBasico()
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

# Decoración compleja
cafeloco = Azucar(Leche(Azucar(Leche(cafe))))
print(cafeloco.descripcion())  # café básico con leche con azúcar con leche con azúcar
print(cafeloco.costo())        # 5.80 (1.00 + 1.50 + 0.90 + 1.50 + 0.90)