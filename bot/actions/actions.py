from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.forms import FormAction
import requests
import re
import json



class ActionOTRS(Action):

    def name(self):
        return "action_otrs"

    def run(self, dispatcher, tracker, domain):
            dispatcher.utter_message('Mensagem enviada por uma custom action teste')

class SearchOnStackoverflow(Action):

    def name(self):
        return "action_search_on_stackoverflow"

    def run(self, dispatcher, tracker, domain):
        question = re.search(r'(buscar|pesquisar)\s(.*)no*\s*([sS]tack\s?[oO]verflow)', tracker.latest_message['text']).group(2)
        #split = question.split(' ')
        #if(len(split) > 1):
        #    separator = '%3B'
        #    question = separator.join(split)

        url = 'https://api.stackexchange.com/2.2/search'
        order = 'desc'
        sort = 'activity'
        intitle = question
        site = 'stackoverflow'

        payload = {
            'order': order, 'sort': sort, 'intitle': intitle, 'site': site
        }

        res = requests.get(url, params=payload)
        data = json.loads(res.text)
        try:
       # data = json.loads(res.text)
            botResponse = 'Aqui está: ' + data['items'][0]['link']
            dispatcher.utter_message(botResponse)
        except:
            botResponse = 'Infelizmente não encontrei nada sobre ' + question +' no StackOverflow. Tente escrever de forma mais compacta e em inglês,             para refinar a busca!'
            dispatcher.utter_message(botResponse)
