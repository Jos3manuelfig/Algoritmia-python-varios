def mi_decorador(func):
    def envoltura():
        print("Antes de ejecutar la función")
        resultado = func()  # Ejecutamos y capturamos el resultado
        print("Después de ejecutar la función")
        return resultado  # Retornamos el resultado de `func`
    return envoltura

@mi_decorador
def saludar():
    print("¡Hola!")
    return "Mensaje retornado"

# Llamamos a la función decorada
resultado = saludar()
print(f"Resultado de la función decorada: {resultado}")