def Operacion(oper):
    multiplicar= oper * 100
    sumar= oper+ 100
    return multiplicar ,sumar
var= int(input('Introduzca un Valor: '))
mul, sum = Operacion(var)

print(f' Valor 1 : {mul} valor 2: {sum}')