class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age  # Se llama al setter

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("La edad no puede ser negativa")
        self._age = value

# Crear objeto
person = Person("Juan", 30)
print(person.age)  # Output: 30

person.age = 35  # Cambia la edad
print(person.age)  # Output: 35

# Intentar una edad inválida
try:
    person.age = -10
except ValueError as e:
    print(e)  # Output: La edad no puede ser negativa