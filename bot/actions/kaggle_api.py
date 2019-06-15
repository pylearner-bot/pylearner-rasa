import os
#import commands
import subprocess
import json
#var = os.system("ls")
var = subprocess.getoutput("kaggle competitions list --category gettingStarted")
#var = 'goku           gohan vegeta picolo bruno gohan'

count = 0
bar = False
var1 = ''
#var1 += 'a'
for c in var:
    if(c == '\n'): count +=1
    if (count <= 2): continue
    if (bar): var1 += c
    bar = True    
#print (var1)
#var1 = '15:00 2010:25 25:0 1:0 1:0 1:0 1:0 1:0'

#print (var1.split('\n')[0])
names = []
for c in var1.split('\n'):
    competition, date_start, date_end, category, complement, reward, teamCount, bol = c.split()
    names.append(competition)

url = 'https://www.kaggle.com/c/'
url1 = '/overview'
for n in names:
    print (url + n + url1)
    
