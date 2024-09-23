class cuenta:
    def __init__ (self, titular,saldo):
        self.titular= titular
        self.saldo = saldo
    
    
    def depositar (self, cantidad):
         self.saldo+=cantidad
         print('se Deposito: ', cantidad)
         
    def Retirar(self, cantidad):
          self.saldo-=cantidad
          print('se Retiro : ',cantidad)
     
    def Mostrar(self):
          print(self.__dict__)
          
          
cliente=cuenta('Jose Figuera',1000)
cliente.Mostrar()
cliente.depositar(500)
cliente.Mostrar()

    
     