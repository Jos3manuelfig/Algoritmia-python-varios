class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

    def establecer_edad(self, nueva_edad):
        if 0 < nueva_edad < 120:  # Validación simple de edad
            self.__edad = nueva_edad
        else:
            print("Edad inválida.")

# Uso de la clase
persona = Persona("Ana", 30)
print(persona.obtener_nombre())  # Muestra: Ana
print(persona.obtener_edad())    # Muestra: 30

persona.establecer_edad(35)      # Cambia la edad a 35
print(persona.obtener_edad())    # Muestra: 35

persona.establecer_edad(150)     # Intento de establecer una edad inválida
# Muestra: Edad inválida.