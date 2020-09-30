#!/usr/bin/env python3

#Imports and dependencies

import requests
from bs4 import BeautifulSoup

def download_article():

    #The content is written into a text file

    file = open("Medium_article_content.txt", "w")

    #The URL of the article is entered here
    page_url = input("Enter the URL of the Medium Article ")

    #On looking for "my user agent", can be used to retrieve the value"
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'} 

    response = requests.get(page_url)

    soup = BeautifulSoup(response.text,"html.parser")

    #The content of the article is stored in the <article> tag

    for line in soup.find('article').find('div'):
  
    #All the content is essentially stored between <p> tags
  
        for content in line.find_all('p'):

        #contents are written into a file
    
            file.write(content.text + '\n')

    file.close()

if __name__ == "__main__":
    download_article()
