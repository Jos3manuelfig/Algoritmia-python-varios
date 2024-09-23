def es_par(n):
    if n %2== 0:
        return f' el numero ingresado es Par'
    return f'el numero es impar'
try:  
    num=int(input('Introduzca un Numero: '))

    resultado=es_par(num)
    print(resultado)
except:
    print('ingrese un valor numerico')