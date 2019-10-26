import urllib.request
from bs4 import BeautifulSoup

URL = "http://univ.cc/search.php?dom=world&key=&start="

LAST_PAGE_NUMBER = 7551

#function to read 
def read_page(pageLink,pageCount):
  links = []
  try:
    resp = urllib.request.urlopen(pageLink+str(pageCount))
    soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
    for link in soup.find("ol", {"start":pageCount}).find_all('a', href=True):
      links.append(str(link.get_text())+','+link['href'])
  except:
    pass
  return links

def main():
  file_name="universities"
  with open(file_name+".csv","w") as file:
    for page_number in range(1,LAST_PAGE_NUMBER,50):
      links = read_page(URL,page_number)
      
      percent = int((page_number/LAST_PAGE_NUMBER)*100)
      percent_left = int(((LAST_PAGE_NUMBER-page_number)/LAST_PAGE_NUMBER)*100)
      print(str(percent)+"% done "+str(percent_left)+"% left")
      
      for link in links:
        try:
          file.write(link+"\n")
        except:
          pass

if __name__ == "__main__":
  main()
