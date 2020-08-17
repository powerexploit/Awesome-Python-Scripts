# In this script we will automate Google using Selenium 

# Imports : 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
 
driver = webdriver.Chrome(ChromeDriverManager().install())

# enter the link of the google
driver.get("http://www.google.com")

# AUTOMATING CLICKING OF THE LINK TEXT

# enter the name of the text
element = driver.find_element_by_link_text("About")

# delaying by 2 sec
time.sleep(2)
# clicking of the element is done by the below click method
element.click()
time.sleep(5)

# AUTOMATING CLICKING OF BACKWARD AND FOORWARD BUTTON  

# going backward
driver.back()

time.sleep(5)

# going forward 
driver.forward()

# AUTOMATING THE REFRESH OF THE WEBPAGE
time.sleep(10)
driver.refresh()
