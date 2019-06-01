from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import re
# from rasa_core_sdk.events import SlotSet
import requests
import json
import pandas as pd
# import random


class ActionOTRS(Action):

    def name(self):
        return "action_otrs"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message("Mensagem enviada por uma custom action.")
        except ValueError:
            dispatcher.utter_message(ValueError)

    def createTicket(self, dispatcher, tracker, domain):
        return

    def closeTicket(self, dispatcher, tracker, domain):
        return

class SearchOnStackoverflow(Action):

    def name(self):
        return "action_search_on_stackoverflow"

    def run(self, dispatcher, tracker, domain):
        question = re.search(r'(buscar|pesquisar)\s(.*)no*\s*([sS]tack\s?[oO]verflow)', tracker.latest_message.text).group(2)
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
        data = pd.read_json(res.text)
        botResponse = 'Aqui está: ' + data.loc[0][0]['link']
        dispatcher.utter_message(botResponse)

