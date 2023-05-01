import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://google.com/')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
# Getting the title tag
print(soup.title.get_text())
