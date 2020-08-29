
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait



def getLocation():

    options = Options()

    options.add_argument("--use-fake-ui-for-media-stream")

    timeout = 20

    driver = webdriver.Chrome(executable_path = './chromedriver.exe', options=options)

    driver.get("https://mycurrentlocation.net/")

    wait = WebDriverWait(driver, timeout)

    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')

    longitude = [x.text for x in longitude]

    longitude = str(longitude[0])

    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')

    latitude = [x.text for x in latitude]

    latitude = str(latitude[0])

    driver.quit()

    return (latitude,longitude)

r = getLocation()
import reverse_geocoder as rg 
import pprint
x = str()

def reverseGeocode(coordinates): 
    result = rg.search(coordinates) 
      
    # result is a list containing ordered dictionary. 
    pprint.pprint(result)
    print(result)
    d = dict(result[0])
    x = d['name']
    print(x)    
  
# Driver function

if __name__=="__main__": 
      
    # Coorinates tuple.Can contain more than one pair. 
    coordinates = r
      
    reverseGeocode(coordinates) 

