import requests


characters = ['Hulk', 'Captain America', 'Thanos']
url = 'https://akabab.github.io/superhero-api/api/'
characters_info = {}
all_characters = requests.get(url + '/all.json').json()
for character_dict in all_characters:
 if character_dict['name'] in characters:
  characters_info[character_dict['name']] = character_dict['powerstats']['intelligence']
print(max(characters_info, key=characters_info.get))



