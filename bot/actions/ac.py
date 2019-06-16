from rasa_core_sdk import Action
import re
# from rasa_core_sdk.events import SlotSet
import requests
import json
# import random

latest_message = 'buscar como remover arquivos no git no stack overflow'
question = re.search(r'(buscar|pesquisar)\s(.*)no*\s*([sS]tack\s?[oO]verflow)', latest_message).group(2)
#split = question.split(' ')
    
#if(len(split) > 1):
    #separator = '%3B'
    #question = separator.join(split)
print(question)
question = 'plot histogram'

link = 'https://api.stackexchange.com/2.2/search'
order = 'desc'
sort = 'activity'
#intitle = 'how can I delete a file from git repo'
intitle = question
site = 'stackoverflow'

payload = {
    'order': order, 'sort': sort, 'intitle': intitle, 'site': site
        }

result = requests.get(link, params=payload)
dictionary = json.loads(result.text)
print(dictionary)


