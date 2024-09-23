import requests

def get_pokemon_info(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Error: {response.status_code}')
        return None

pokemon_name = input('Ingrese el nombre de un Pokémon: ')
pokemon_info = get_pokemon_info(pokemon_name)
if pokemon_info:
    print(f'Nombre: {pokemon_info["name"]}')
    print(f'Altura: {pokemon_info["height"]}')
    print(f'Peso: {pokemon_info["weight"]}')
    print('Tipos:')
    for type_data in pokemon_info['types']:
        print(f'- {type_data["type"]["name"]}')