import requests
from bs4 import BeautifulSoup

# TODO: url from online
url = 'http://quotes.toscrape.com/'

# TODO: store information from url to response
response = requests.get(url)
# TODO: write the response text as lxml form and assign to soup variable
soup = BeautifulSoup(response.text, 'lxml')
# TODO: get all class='text' and tag is span
quotes = soup.find_all('span', class_='text')
'''
soup has all value
.find_all(tag, class) will find all value which match to the parameter including tag and text inside tag
'''
# TODO: big tag and small tag detail
tags = soup.find_all('div',class_='tags')

# TODO: finding the author
authors = soup.find_all('small',class_='author')

# TODO: print author and quote only text
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)