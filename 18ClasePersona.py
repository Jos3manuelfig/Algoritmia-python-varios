class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear un objeto de la clase Persona
persona1 = Persona("José", 25)

# Acceder a los atributos del objeto
print(persona1.nombre)  # José
print(persona1.edad)  # 25


# Llamar a un método del objeto
persona1.saludar()  # Hola, soy José y tengo 25 años.




    