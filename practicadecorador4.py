def envoltura(func):
    def saludar():
        print('Hola, primer saludo')
        #resultado = func()  # Llamamos a la función decorada
        print('Adiós, segundo saludo')
        return func()# Devolvemos el resultado de la función decorada
    return saludar  # Devolvemos la función interna

@envoltura
def segundo_saludo():
    return 'Segundo saludo'

print(segundo_saludo())