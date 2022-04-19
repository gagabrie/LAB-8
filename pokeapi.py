import requests 

def get_pokemon_info(name):
    """
    Gets a dictionary of info from the PokeAPI for a pokemon.
    
    :param name: Pokemon's name (or poke index)
    """

    print("Getting user information...", end='')
    if name is None:
        return

    name = name.lower()
    if name == '':
        return

    URL = 'https://pokeapi.co/api/v2/pokemon/' + str(name)
    response = requests.get(URL)

    if response.status_code == 200:
        print('success')
        return response.json() 
    else:
        print('failed. Response code:', response.status_code)
        return