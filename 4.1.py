import requests
from bs4 import BeautifulSoup

output = {}
r = requests.get('https://theinternship.io/')
s = BeautifulSoup(r.content, 'html.parser')
data = s.find('div', {'class': 'columns is-multiline'})

a_tags = data.find_all('a')
des = data.find_all('span')

for i in range(len(a_tags)):
    output[des[i].text] = a_tags[i].find('img')['src']

for j in sorted(output, key = lambda j: len(j), reverse = True):
    print(output[j])
