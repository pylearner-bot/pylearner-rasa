import re
import requests
import json


latest_message = 'buscar api machine learning no towardsdatascience'

question = re.search(r'(buscar|pesquisar)\s(.*)no*\s*([tT]owards?\s?[dD]ata[sS]cience)', latest_message).group(2)

print(question)

link = 'https://www.googleapis.com/customsearch/v1?key='
api_key = 'AIzaSyD2q63xBdRyjur_Z5aR6MxWu6xI66YNuj0'
operator = '&'
cx = 'cx=' + '014903448052095461784:jlpfd5trt48'
query = 'q=' + question

api_format = link + api_key + operator + cx + operator + query

print(api_format)

result = requests.get(api_format)

data = json.loads(result.text)

try:
    print (data)

except:
    print (data)
