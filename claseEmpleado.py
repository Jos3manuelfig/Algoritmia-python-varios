class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        
    def salario_anual(self):
        return self.salario * 12
      
    def mostrar_info(self):
        print(f'Empleado: {self.nombre} \nSalario Anual: {self.salario_anual()}')


class Gerente(Empleado):
         def __init__(self, nombre, salario,bono):
          super().__init__(nombre,salario)
          self.bono=bono
         def salario_anual(self):
              salario_a=super().salario_anual()
              return salario_a + self.bono
              
         def mostrar_info(self):
                super().mostrar_info() 
                print(f'Bono: {self.bono}')                 
                
                           
                                    
                                                      
E1 = Empleado('Jose', 1000)
E1.mostrar_info()
E2=Gerente('Figuera', 5000,1000)
E2.mostrar_info()
