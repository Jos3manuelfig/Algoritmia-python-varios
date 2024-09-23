def es_email_valido(email):
    # Verifica si el correo tiene un símbolo @
    if '@' not in email:
        return False

    # Separa el correo en dos partes usando el símbolo @
    usuario, dominio = email.split('@', 1)

    # Verifica que la parte del usuario y del dominio no estén vacías
    if not usuario or not dominio:
        return False

    # Verifica que el dominio contenga un punto
    if '.' not in dominio:
        return False

    # Separa el dominio por el punto y verifica que cada parte tenga contenido
    partes_dominio = dominio.split('.')
    if any(not parte for parte in partes_dominio):
        return False

    # Verifica que el dominio no termine en un punto
    if dominio[-1] == '.':
        return False

    # Si todas las verificaciones son correctas, el correo es válido
    return True

# Pruebas de la función
print(es_email_valido('ejemplo@dominio.com'))  # Debería retornar True
print(es_email_valido('noesvalido@dominio'))   # Debería retornar False
print(es_email_valido('nada@.com'))            # Debería retornar False
print(es_email_valido('nada@dominio.'))        # Debería retornar False
print(es_email_valido('@dominio.com'))         # Debería retornar False
