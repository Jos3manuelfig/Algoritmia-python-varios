class Validator:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_valid_password(self):
        # Verificar longitud mínima de 8 caracteres
        if len(self.password) < 8:
            return False

        # Verificar si hay al menos 2 caracteres especiales
        special_chars = "!@#$%^&*(),.?\":{}|<>"
        special_count = 0
        for char in self.password:
            if char in special_chars:
                special_count += 1
        if special_count < 2:
            return False

        # Verificar si hay al menos 1 mayúscula
        has_uppercase = False
        for char in self.password:
            if char.isupper():
                has_uppercase = True
                break
        if not has_uppercase:
            return False

        return True

# Ejemplo de uso
username = "user123"
password = "Passw@rd1!"

validator = Validator(username, password)

if validator.is_valid_password():
    print("El password es válido.")
else:
    print("El password no es válido.")