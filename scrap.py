from bs4 import BeautifulSoup
import re
import requests
import json

file = open('SouqDataapple.json','w',encoding='utf8')
url = "https://www.leewayhertz.com/" 
data = {}

links=[]
req=requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

htmlData=soup.findAll('a',)

file.write('[\n')

for link in htmlData:
    if link.get('href') !=None:    
        links.append(link.get('href'))
        data['link'] =link.get('href')
        json_data = json.dumps(data,ensure_ascii=False)
        file.write(json_data)
        file.write(",\n")         

file.write("\n]")

