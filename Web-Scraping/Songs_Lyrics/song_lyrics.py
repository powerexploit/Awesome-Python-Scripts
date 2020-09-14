import requests
from bs4 import BeautifulSoup


def get_lyrics(artist, song):
    base_url = 'http://www.azlyrics.com/'
    song_url = 'http://www.azlyrics.com/lyrics/' + artist + '/' + song + '.html'

    # Use requests library to get html from artist's page
    response = requests.get(song_url)

    # Make the html soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
    	lyrics = soup.find('div' , class_ = 'col-xs-12 col-lg-8 text-center').find_all('div')[5].text
	print(lyrics)
    except AttributeError:
	print("Either this song doesnt exist or make sure you have entered the correct spelling!!")


artist = input("Enter the name of the artist/band ")
song = input("Enter the name of the song ")
get_lyrics(artist, song)
