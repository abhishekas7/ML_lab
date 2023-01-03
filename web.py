import requests
from bs4 import BeautifulSoup
URL="http://www.ajce.in"
r=requests.get(URL)
Soup=BeautifulSoup(r.content,'html.parser')
print(Soup)