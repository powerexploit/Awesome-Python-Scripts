import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import numpy as np
import itertools
import time


class Scrap:

    def __init__(self, urls_dict, start_date='2020-01-01', end_date='2020-08-01', number=10, year=2020):
        self.urls = urls_dict
        self.start = pd.to_datetime(start_date)
        self.end = pd.to_datetime(end_date)
        self.n = number
        self.year = year
        self.titles = []
        self.sub_titles = []
        self.article_link = []
        self.claps = []
        self.reading_time = []
        self.responses = []
        self.pubs = []
        self.dates_list = []
        
    def randDates(self):
        start_u = self.start.value//10**9
        end_u = self.end.value//10**9

        return pd.DatetimeIndex((10**9*np.random.randint(start_u, end_u, self.n, dtype=np.int64)).view('M8[ns]')).date

    def scrap(self):
        dates = pd.to_datetime(pd.Series(self.randDates()))
        for i in range(len(dates)):
            month = dates.dt.month[i]
            day = dates.dt.day[i]
            for publication, url in self.urls.items():
                url = url+'/archive/{0}/{1:02d}/{2:02d}'
                print(f'Publication: {publication}, Date: {self.year}-{month}-{day}')
                response = requests.get(url.format(self.year, month, day), allow_redirects=True)
                if not response.url.startswith(url.format(self.year, month, day)):
                    continue
                page = response.content
                soup = BeautifulSoup(page, 'html.parser')
                articles = soup.find_all("div", class_="postArticle postArticle--short js-postArticle js-trackPostPresentation js-trackPostScrolls")
                
                number = len([i.find('h3',class_="graf--title" ).text if i.find('h3',class_="graf--title" ) is not None else '' for i in articles])
                
                self.titles.append([i.find('h3',class_="graf--title" ).text if i.find('h3',class_="graf--title" ) is not None else '' for i in articles])

                self.sub_titles.append([i.find("h4", class_="graf--subtitle").text if i.find("h4", class_="graf--subtitle") is not None else '' for i in articles])

                self.article_link.append([i.find_all('a')[3]['href'].split('?')[0] for i in articles])

                self.claps.append([0 if (k is None) or (k == '') or (k.split is None) else int(float(k.split('K')[0])*1000) if len(k.split('K'))==2 else int(float(k.split('K')[0])) for k in [j.text for j in [i.find_all('button')[1] for i in articles]]])

                self.reading_time.append([int(i.find("span", class_="readingTime")['title'].split()[0]) if i.find("span", class_="readingTime") is not None else 0 for i in articles])

                self.responses.append([i.find_all('a')[6].text.split(' ')[0] if (len(i.find_all('a'))==7) and len(i.find_all('a')[6].text.split(' '))!=0 else 0 for i in articles])
                
                self.pubs.append([publication]*number)

                self.dates_list.append([f'{self.year}-{month}-{day}'])
                
                time.sleep(0.3)

    def dataframe(self):
        columns = ['Title', 'SubTitle', 'Link', 'Claps', 'Reading_Time', 'Responses', 'Publication','Date_Published']
        titles = list(itertools.chain.from_iterable(self.titles))
        sub_titles = list(itertools.chain.from_iterable(self.sub_titles))
        article_link = list(itertools.chain.from_iterable(self.article_link))
        claps = list(itertools.chain.from_iterable(self.claps))
        reading_time = list(itertools.chain.from_iterable(self.reading_time))
        responses = list(itertools.chain.from_iterable(self.responses))
        pubs = list(itertools.chain.from_iterable(self.pubs))
        dates = list(itertools.chain.from_iterable(self.dates_list))

        return pd.DataFrame(zip(titles, sub_titles, article_link, claps, reading_time, responses, pubs, dates), columns=columns)
