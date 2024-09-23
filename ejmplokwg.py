def read_dict_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} - {value}")

# Ejemplo de uso
print("Primer llamado:")
read_dict_args(name1="Ricardo", name2="Ramon", web="jarroba.com")

print("\nSegundo llamado:")
read_dict_args(Team="FC Barcelona", player="Iniesta", demarcation="Right winger", number=8)
