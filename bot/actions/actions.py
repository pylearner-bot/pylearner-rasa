from rasa_core_sdk import Action
import re
# from rasa_core_sdk.events import SlotSet
import requests
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
    
class ActionSearchOnStackoverflow(Action):

    def name(self):
        return "action_search_on_stackoverflow"

    def run(self, dispatcher, tracker, domain):
        question = re.search(r'(buscar|pesquisar)\s(.*)(no)*\s*([sS]tack\s?[oO]verflow)', tracker.latest_message.text).group[2]
        URL = 'https://api.stackexchange.com/docs/advanced-search#order=desc&sort=relevance&accepted=True&tagged=python%3B'+ question + '&filter=default&site=stackoverflow'
        res = requests.get(url = URL)
        data = res.json()
        dispatcher.utter_message('Aqui está: ' + data[0].link)
        return 
    
