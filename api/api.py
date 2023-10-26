# ChooseYourPokemon/api/api.py
import random
import requests

def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    print(response)
    pokemon = response.json()
    stats = {
    'name': pokemon['name'],
    'id': pokemon['id'],
    'base_experience': pokemon['base_experience'],
    'height': pokemon['height'],
    'weight': pokemon['weight'],
    }
    return stats
