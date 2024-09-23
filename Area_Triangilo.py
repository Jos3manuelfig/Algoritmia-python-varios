def Area_Triangulo(base,altura):
    return base*altura/2
    
a=float(input('Introduzca base: '))  
b=float(input('Introduzca altura: '))

re= Area_Triangulo(a,b)
print(f'El Area es: {re}')    
