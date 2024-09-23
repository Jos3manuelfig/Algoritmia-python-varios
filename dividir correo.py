email = ['josemanuelfg1983@gmail.com']

# Asegúrate de que el correo esté en formato de cadena (no en una lista)
correo = email[0]

# Dividimos el correo en dos partes utilizando el símbolo '@'
parte_anterior, parte_posterior = correo.split('@')

# Imprimimos las partes resultantes
print(f"Primera parte: {parte_anterior}")
print(f"Segunda parte: {parte_posterior}")
