from bs4 import BeautifulSoup
import requests

#The instagram URL
URL="https://www.instagram.com/{}/"
username = input(" Enter the instagram username ")

#request a response from the URL
response = requests.get(URL.format(username))
# scraping the contents
soup = BeautifulSoup(response.text,"html.parser")
#The contents of the meta tag with the property og:description are accessed here
meta_content = soup.find("meta", property="og:description") 
#print(meta_content)
data = {}
content = meta_content.attrs['content']
content = content.split("-")[0]
content = content.split(" ")

data['Followers'] = content[0]
data['Following'] = content[2]
data['Posts'] = content[4]

print(username + " has " + data["Followers"]+" followers, "+ data["Following"]+" following, "+ data["Posts"]+" posts ")


'''
output:
 Enter the instagram username "ferrari"
 ferrari has 19m followers, 5 following, 2,538 posts 
'''
