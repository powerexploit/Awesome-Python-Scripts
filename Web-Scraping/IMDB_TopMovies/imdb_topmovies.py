# -*- coding: utf-8 -*-
"""IMDB_Topmovies.ipynb
"""

#scrap top 250 movies from IMDB and generate a CSV file for it using beautifulsoup

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html')
 
movies = soup.select('td.titleColumn')
stars = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [round(float(b.attrs.get('data-value')),1) for b in soup.select('td.posterColumn span[name=ir]')]
 
imdb = []
 
# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, len(movies)):
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    data = {"movie_title": movie_title,
            "year": year,
            "star_cast": stars[index],
            "rating": ratings[index],
            }
    imdb.append(data)
 
# CREATING A DATAFRAME
df = pd.DataFrame(imdb)
df.index = df.index.rename('S.No')
#copy data frame in to CSV file
#csv file has been created in current working directory
df.to_csv('imdb.csv')
#read=pd.read_csv('/content/imdb.csv') 
#print(read)
