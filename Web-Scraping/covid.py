#webscrapping which webscrapes data from the worldometers website and collects various stats releated to covid 19 and stores in the csv format 
#website:https://www.worldometers.info/coronavirus/
import requests
import csv
from bs4 import BeautifulSoup

f=csv.writer(open('covid.csv','w'))
#f.writerow(['country_other','total_cases','new_cases','total_death','new_death','total_recovered','active_cases','serious','tot_cases','total_death'])
url='https://www.worldometers.info/coronavirus/'
page=requests.get(url) #requests the page through the url
page=BeautifulSoup(page.text,'html.parser')  #parses the text by html.parser
content=page.find(class_='main_table_countries_div')
content_data=content.find_all('tr')
for data in content_data:
	country_other=(data.contents[1].text)
	total_cases=(data.contents[3].text)
	new_cases=(data.contents[5].text)
	total_death=(data.contents[7].text)
	new_death=(data.contents[9].text)
	total_recovered=(data.contents[11].text)
	active_cases=(data.contents[13].text)
	serious=(data.contents[15].text)
	tot_cases=(data.contents[17].text)
	total_death=(data.contents[19].text)
	f.writerow([country_other,total_cases,new_cases,total_death,new_death,total_recovered,active_cases,serious,tot_cases,total_death])

#after the script gets executed the stats gets saved in the csv file