import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.dowellcomputer.com/main.jsp")

html = request.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select('td > a')
for link in links:
    if link.has_attr('href'):
        if link.get('href').find('notice') != -1:
            print(link.text)
