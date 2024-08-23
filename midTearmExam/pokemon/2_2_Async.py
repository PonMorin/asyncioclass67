import asyncio
import httpx
import time

async def get_pokemon(client, url):
    print(f"{time.ctime()} - get {url}")
    resp = await client.get(url)
    pokemon_ability = resp.json()
    pokemon_names = []
    for pokemon in pokemon_ability['pokemon']:
        pokemon_names.append(pokemon['pokemon']['name'])
    return pokemon_names

async def get_pokemons(ability):
    start_time = time.perf_counter()
    async with httpx.AsyncClient() as client:
        url = f'https://pokeapi.co/api/v2/ability/{ability}'
        pokemon_names = await get_pokemon(client, url)
        end_time = time.perf_counter()
        print(f"{time.ctime()} - {pokemon_names}")
        print(f"{time.ctime()} - Asynchronous get {len(pokemon_names)} pokemons. Time taken: {end_time-start_time} seconds")
        return pokemon_names

async def index():
    # start_time = time.perf_counter()
    list_ability = ['battle-armor', 'speed-boost']
    coro = [get_pokemons(i) for i in list_ability]
    result = await asyncio.gather(*coro)

if __name__ == '__main__':
    asyncio.run(index())
