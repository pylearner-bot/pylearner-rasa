from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random
import json

class Action_cross_validated(Action):

    def name(self):
        return "action_cross_validated"

    def run(self,dispatcher,tracker,domain):

        intitle = tracker.get_slot('questions')

        URL = 'https://api.stackexchange.com/2.2/search'
        order = 'desc'
        sort = 'activity'
        site = 'stats'

        payload = {
            'order': order, 'sort': sort, 'intitle': intitle, 'site': site
        }

        response = requests.get(URL, params=payload)
        data = json.loads(response)
        bot_response = "Aqui esta: " + data[0].link

        try:
            dispatcher.utter_message(bot_response)
        except:
            dispatcher.utter_message(ValueError)
