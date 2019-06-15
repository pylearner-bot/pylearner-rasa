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
        question = ''
        if re.search(r'(buscar|pesquisar)\s(.*)no*\s*([sS]tack\s?[oO]verflow)', tracker.latest_message['text']):
            question = re.search(r'(buscar|pesquisar)\s(.*)no*\s*([sS]tack\s?[oO]verflow)', tracker.latest_message['text']).group(2)

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
        links = self.validate_answered(data)
        if links:
            dispatcher.utter_message('Aqui está: ')
            for link in links:
                # botResponse = 'Aqui está: ' + data['items'][0]['link']
                dispatcher.utter_message(link)
        else:
            botResponse = 'Infelizmente não encontrei nada sobre ' + question +' no StackOverflow. Tente escrever de forma mais compacta e em inglês para refinar a busca!'
            dispatcher.utter_message(botResponse)
            dispatcher.utter_message('Tente escrever desta forma:')
            dispatcher.utter_message('pesquisar [sua dúvida] no stackoverflow')
    
    def validate_answered(self, data):
        links = []
        for item in data['items']:
            if str(item['is_answered']) == 'True':
                links.append(item['link'])
            if len(links) == 3:
                break
        return links


class SearchOnCrossValidated(Action):

    def name(self):
        return "action_search_on_crossvalidated"

    def run(self, dispatcher, tracker, domain):
        question = ''
        if re.search(r'(buscar|pesquisar)\s(.*)no*\s*([cC]ross\s?[vV]alidated)', tracker.latest_message['text']):
            question = re.search(r'(buscar|pesquisar)\s(.*)no*\s*([cC]ross\s?[vV]alidated)', tracker.latest_message['text']).group(2)

        url = 'https://api.stackexchange.com/2.2/search'
        order = 'desc'
        sort = 'activity'
        intitle = question
        site = 'crossvalidated'

        payload = {
            'order': order, 'sort': sort, 'intitle': intitle, 'site': site
        }

        res = requests.get(url, params=payload)
        data = json.loads(res.text)
        links = self.validate_answered(data)
        if links:
            dispatcher.utter_message('Aqui está: ')
            for link in links:
                # botResponse = 'Aqui está: ' + data['items'][0]['link']
                dispatcher.utter_message(link)
        else:
            botResponse = 'Infelizmente não encontrei nada sobre ' + question +' no Cross Validated. Tente escrever de forma mais compacta e em inglês para refinar a busca!'
            dispatcher.utter_message(botResponse)
            dispatcher.utter_message('Tente escrever desta forma:')
            dispatcher.utter_message('pesquisar [sua dúvida] no crossvalidated')

    def validate_answered(self, data):
        links = []
        for item in data['items']:
            if str(item['is_answered']) == 'True':
                links.append(item['link'])
            if len(links) == 3:
                break
        return links

class SearchOnTowardsDataScience(Action):

    def name(self):
        return "action_search_on_towards_datascience"

    def run(self, dispatcher, tracker, domain):
        question = ''
        if (re.search(r'(buscar|pesquisar)\s(.*)no*\s*([tT]owards?\s?[dD]ata\s?[sS]cience)', tracker.latest_message['text']) != None):
            question = re.search(r'(buscar|pesquisar)\s(.*)no*\s*([tT]owards?\s?[dD]ata\s?[sS]cience)', tracker.latest_message['text']).group(2)            
        
        link = 'https://www.googleapis.com/customsearch/v1?key='
        api_key = 'AIzaSyD2q63xBdRyjur_Z5aR6MxWu6xI66YNuj0'
        operator = '&'
        cx = 'cx=' + '014903448052095461784:jlpfd5trt48'
        query = 'q=' + question
        api_format = link + api_key + operator + cx + operator + query
        result = requests.get(api_format)
        data = json.loads(result.text)

        try:
            cont = 0
            dispatcher.utter_message('Aguarde um momento irei pesquisar sobre' + question + 'no Towards Data Science...')
            for link in data['items']:
                if cont == 4: break
                dispatcher.utter_message(link['link'])
                cont += 1            
            dispatcher.utter_message('Encontrei estes links que falam sobre ' + question + '! Espero que auxiliem no seu aprendizado. Enfim, bons estudos!') 
        
        except:
            dispatcher.utter_message ('Infelizmente não encontramos nada relacionado a isso no Towards Data Science')
            dispatcher.utter_message ('Tente escrever em inglês para refinar sua busca e da seguinte forma:')
            dispatcher.utter_message ('pesquisar [what you want] no towardsdatascience')
