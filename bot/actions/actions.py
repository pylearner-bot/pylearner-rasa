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
        links = self.validate_answers(data)

        if links:
            dispatcher.utter_message('Aqui está:')
            for link in links:
                dispatcher.utter_message(link)

        else:
            dispatcher.utter_message(
            'Desculpe, mas não encontrei nada sobre o que você pediu.' +
            'Quer tentar com outras palavras?')
        return []
