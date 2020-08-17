# In this script we will automate Google Search using Selenium

# Imports : 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

# providing the link  
driver.get("http://www.google.com")

# then we will look for the search bar name(here name is referred to the html code)
element = driver.find_element_by_name("q")

# this is to provide some delay so that we can easily see the process
time.sleep(2)
element.clear()

# here whatever we have to search we can write between the parenthesis
element.send_keys("Python")

# for the enter button
element.send_keys(Keys.RETURN)
