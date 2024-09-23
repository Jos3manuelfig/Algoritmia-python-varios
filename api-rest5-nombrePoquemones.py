import requests

def get_first_10_pokemon_names():
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=10'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemon_names = [pokemon['name'] for pokemon in data['results']]
        return pokemon_names
    else:
        print(f'Error: {response.status_code}')
        return None

pokemon_names = get_first_10_pokemon_names()
if pokemon_names:
    for name in pokemon_names:
        print(name)