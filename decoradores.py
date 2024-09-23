def llamar_function(function):
    def wrapper():
        print(f'La función {function.__name__} ha sido llamada...!')
        return function
    return wrapper

@llamar_function            
def function1():
    pass

# Si quieres decorar otras funciones, debes usar el mismo decorador:
@llamar_function
def function2():
    pass

@llamar_function
def function3():
    pass

# Ahora si llamas a function1, function2, o function3, deberías ver el mensaje en la consola.
function1()
function2()
function3()