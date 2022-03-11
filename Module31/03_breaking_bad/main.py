import json, requests

my_req = requests.get('https://www.breakingbadapi.com/api/deaths')  # Список погибших
general_death_req = requests.get('https://www.breakingbadapi.com/api/death-count')  # Парсинг общего числа смертей
episodes_req = requests.get('https://www.breakingbadapi.com/api/episodes')

data = json.loads(my_req.text)
deathCount = json.loads(general_death_req.text)
episodes = json.loads(episodes_req.text)

number_of_deaths = max(data, key=lambda elem: elem['number_of_deaths'])

list_of_death = list(map(lambda x: x['death'], data))

episode_id = {}
for i_elem in episodes:
    if i_elem['episode'] == str(number_of_deaths['episode']) and i_elem['season'] == str(number_of_deaths['season']):
        episode_id = i_elem
        break

print('ID эпизода:', episode_id['episode_id'])
print('Номер сезона:', number_of_deaths['season'])
print('Номер эпизода:', number_of_deaths['episode'])
print('Общее число смертей:', deathCount[0]['deathCount'])
print('Список погибших:', ', '.join(list_of_death))

result = {'episode_id': episode_id['episode_id'],
          'season': number_of_deaths['season'],
          'episode': number_of_deaths['episode'],
          'deathCount': deathCount[0]['deathCount'],
          'death:': list_of_death
          }

with open('Breaking_Bad.json', 'w') as file:
    json.dump(result, file, indent=4)