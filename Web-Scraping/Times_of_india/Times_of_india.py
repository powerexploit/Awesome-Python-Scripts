import requests
import datetime
from bs4 import BeautifulSoup

url = "http://timesofindia.indiatimes.com/"

# Use requests library to get html from TOI's page
response = requests.get(url)
# Make the html soup object
soup = BeautifulSoup(response.content, 'html.parser')

print("\t!!!** The Times of India **!!!")
today = datetime.date.today()
print(today.strftime('\tThe date %d, %b %Y'))

# scrping times of India in four domains:
print("\n\t\t**** Flash news ****")
for div in soup.findAll('div', attrs={'id':'featuredstory'}):
    for a in div.findAll('a'):
        print(a.text)

print("\n\t\t**** News in Bulletin ****")
for div in soup.findAll('div', attrs={'class':'top-story'}):
    for a in div.findAll('li'):
        print (a.text)


print("\n\t\t**** Entertainment ****\t")
for div in soup.findAll('div', attrs={'class':'entrmnt-wdgt-outer'}):
    for a in div.findAll('li'):
        print(a.text)
	
 
print("\n\t\t**** Latest News ****\t\n")
for div in soup.findAll('div', attrs={'id':'lateststories'}):
    for a in div.findAll('li'):
        print(a.text)
