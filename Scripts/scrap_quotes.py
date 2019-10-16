from bs4 import BeautifulSoup
import requests
import json
base_url="https://www.goodreads.com/quotes/tag/{0}?page={1}"    # the url of the site from where quotes 
#will be scrapped emotion and page number will be inserted later

def process(content,emotion):  # function to clean the content of the webpage 
    soup=BeautifulSoup(content,features="html5lib")
    quotes_div=soup.find_all("div",attrs={"class","quote"}) 
    quotes=[]
    for div in quotes_div:
        q_text=div.find("div",attrs={"class","quoteText"})
        quote=(q_text.text.strip().split('\n')[0])
        author=q_text.find("span",attrs={"class","authorOrTitle"}).text.strip()
        q_dict={"quote":quote,"author":author,"emotion":emotion}
        quotes.append(q_dict)
    return quotes

emotions=['friend','sad']  # you can select any other emotion
quotes=[]
for emotion in emotions:
    for index in range(1,5):  # here 5 pages have been taken 
        final_url=base_url.format(emotion,index)
        page=requests.get(final_url)
        content=page.text
        quotes+=process(content,emotion)

with open('quote.json','w') as file: # dump the quotes in json file
    json.dump(quotes,file)