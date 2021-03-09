import requests
from bs4 import BeautifulSoup

URL = 'https://www.pagina12.com.ar/'

def get_seccions(links):
    for link in links:
        s_request = requests.get(link)
        s_seccion = BeautifulSoup(s_request.text, 'lxml')
        link = s_seccion.find('article', attrs={'class':'article-item article-item--teaser'})
        print(link)
        print('-----------------------')
    # return names, links

request = requests.get(URL)

s = BeautifulSoup(request.text, 'lxml')

seccions = s.find('ul', attrs={'class':'horizontal-list main-sections hide-on-dropdown'}).find_all('li')

links_seccions = [seccion.a.get('href') for seccion in seccions]

get_seccions(links_seccions)

