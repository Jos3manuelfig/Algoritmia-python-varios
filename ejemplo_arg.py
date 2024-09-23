def read_list_args(*args):
    for count, arg in enumerate(args):
        print(f"{count +1} - {arg}")

# Ejemplo de uso
print("Primer llamado:")
read_list_args("Ricardo", "jarroba.com")

print("\nSegundo llamado:")
read_list_args("Ricardo", 23, "Ramon", [1, 2, 3], "jarroba.com")
