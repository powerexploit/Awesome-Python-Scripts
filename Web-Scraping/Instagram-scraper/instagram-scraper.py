#Import all libraries
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# instagram URL
URL="https://www.instagram.com/"

def scrape_data():
    username = input("Enter the instagram username ")
    url=URL+username

    # Sending request to server using Urllib
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_data = urlopen(req).read()

    #Beautyfying all data to html form 
    soup=BeautifulSoup(html_data,'html.parser')

    #Search for meta tag with description of og:description 
    data = soup.find("meta", property="og:description").attrs['content']

    # Split content based on - element
    data = data.split("-")[0]

    # Adding data to user dictionary
    user_data={}
    data = data.split(" ")
    user_data['Followers'] = data[0]
    user_data['Following'] = data[2]
    user_data['Posts'] = data[4]

    return user_data


if __name__=="__main__":
    data=scrape_data()
    print("User has "+data['Followers']+ " Followers")
    print("User is following "+data['Following']+ " peoples")
    print("User has "+data['Posts']+ " Posts")
