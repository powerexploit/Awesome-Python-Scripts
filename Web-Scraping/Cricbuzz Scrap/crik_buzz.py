from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = 'http://www.cricbuzz.com/cricket-match/live-scores'
page = urlopen(URL)
soup = BeautifulSoup(page,'html.parser')

update=[]

for score in soup.find_all('div',attrs={'class':'cb-col cb-col-100 cb-lv-main'}):
	s=score.text.strip()
	update.append(s)

for i in range(len(update)):
	print(i+1),
	print(update[i])

