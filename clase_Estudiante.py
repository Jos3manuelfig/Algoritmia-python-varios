class Estudiante:
    def __init__(self, nom, edad, notas):
        self.nom = nom
        self.edad = edad
        self.notas = notas  # Se inicializa con las notas que se pasan como argumento
        
    def Agregar_Notas(self, califica):
        self.notas.append(califica)
        
    def Promediar_Nota(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        return 0  # Retorna 0 si no hay notas para evitar división por cero
         
    def Mostrar_Notas(self):
        print('Datos de Alumno:\n')
        print(f'Nombre: {self.nom}')
        print(f'Edad: {self.edad}')
        print(f'Notas: {self.notas}')
         
E1 = Estudiante('Jose', 40, [18, 10, 14])

# Agregamos una nota
E1.Agregar_Notas(20)

# Mostramos el promedio de las notas
print(f'Promedio: {E1.Promediar_Nota()}')

# Mostramos la información del estudiante
E1.Mostrar_Notas()