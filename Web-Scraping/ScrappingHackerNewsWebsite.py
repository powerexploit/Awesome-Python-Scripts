'''
Scraping the first 2 pages of Hacker news website which gives lot of Tech news(as a articles)
which has upvotes more than 100.User can just click on story link to see the article.
'''

'''
Program uses requests module to get web data from URL and BeautifulSoup module to parse the web data
as HTML using html parser.
Install requests and BeautifulSoup module before executing!
'''

import requests
from bs4 import BeautifulSoup
import pprint  # prints the Final output in pretty manner which is inbuilt module in Python


response1 = requests.get("https://news.ycombinator.com/news")   #Storing response of first page of website
response2 = requests.get("https://news.ycombinator.com/news?p=2")  # Storing response of Second page of website

response1_html_parser = BeautifulSoup(response1.text,'html.parser') #parsing the received web data by html parser
response2_html_parser = BeautifulSoup(response2.text,'html.parser')

linksInPage1 = response1_html_parser.select('.storylink') #All links of tech news are included in class "Storylink"
linksInPage2 = response2_html_parser.select('.storylink')

votesInPage1 = response1_html_parser.select('.subtext') #All votes are stored inside subclass "score" of class "subtext"
votesInPage2 = response2_html_parser.select('.subtext')


mega_link = linksInPage1 + linksInPage2  # Combining links of both pages
#print(mega_link)
mega_votes = votesInPage1 + votesInPage2

def sorted_stories_list(hackerNewsList):
    """Sorting the list in decreasing order
       with respect to votes"""
    return sorted(hackerNewsList,key=lambda x:x['votes'],reverse=True)

def create_custom_hackernews(mega_link,mega_votes):
    hackerNews =[]
    for index,item in enumerate(mega_link):
        title = mega_link[index].getText()  #To get title of the story(news)
        href = mega_link[index].get('href',None) # To get link of stroy(news).If no link is present, default is None
        vote = mega_votes[index].select('.score') # points are stored inside class "score" of class subtext,if points/votes not available, then class score wont be present.
        if len(vote): #To check if class "score" exists or not
            points = int(vote[0].getText().replace(' points', ''))
            if points > 100:  # To get votes/points more than 100
                hackerNews.append({'title': title, 'link': href,'votes':points})

    return sorted_stories_list(hackerNews)

if __name__ == '__main__':
    # Prints story link, story title and its votes in a pretty manner
    pprint.pprint(create_custom_hackernews(mega_link,mega_votes))