#Imports and dependencies
import re 
import urllib.request 
from bs4 import BeautifulSoup 

def get_lyrics(artist,song_title): 
    
    #The name of the artist and song title are taken as input
    artist = artist.split()
    artist = "".join(artist)
    artist = artist.lower() 
    song_title = song_title.lower() 
    song_title = "".join(song_title)
    song_title = song_title.lower() 

    # remove all except alphanumeric characters from artist and song_title 
    artist = re.sub('[^A-Za-z0-9]+', "", artist) 
    song_title = re.sub('[^A-Za-z0-9]+', "", song_title) 
    if artist.startswith("the"): 
        artist = artist[3:] 
    url = "http://azlyrics.com/lyrics/"+artist+"/"+song_title+".html" 
    
    #The data entered is validated to see if the URL exists, else returns an error message
    try: 
        content = urllib.request.urlopen(url).read() 
        soup = BeautifulSoup(content, 'html.parser') 
        lyrics = str(soup) 
        # the lyrics is contained between the start and end 
        start = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->' 
        end = '<!-- MxM banner -->' 
        lyrics = lyrics.split(start)[1] 
        lyrics = lyrics.split(end)[0] 
        lyrics = lyrics.replace("<br>" , "").replace("<br/>" , "").replace("</i>" ,"").replace("<i>", "").replace("<div>" , "").replace("</div>" , "")
        lyrics = lyrics.strip("\n")
        with open("lyrics.txt" , "w") as f:
            f.write(lyrics)
        return("Lyrics written into a file") 
    except: 
        return("Invalid entry, try again") 

if __name__ == "__main__":
    artist = input("Enter the name of the artist ")
    song_title = input("Enter the title of the song ")
    print(get_lyrics(artist , song_title))
