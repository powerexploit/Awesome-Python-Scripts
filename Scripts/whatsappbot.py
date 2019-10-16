from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from requests import get
from bs4 import BeautifulSoup as bs
import keyboard
import time
import click
import os
import sys
import csv
import threading

chrome_options = Options()
chrome_options.add_argument(
    "user-data-dir=" + os.path.dirname(sys.argv[0]))
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()

driver.get("https://web.whatsapp.com")
# Time to load the QR Code and scenning
time.sleep(25)

# Key in the value of the Chat name that you want to read the messages and reply
target = '"your_friend/group_name"'

# Identify the Chatlist based on its element
panel = driver.find_element_by_class_name('chatlist-panel-body')

elem = None
a = 0
while elem is None:
    a += 300
    try:
        driver.execute_script('arguments[0].scrollTop = %s' % a, panel)
        elem = driver.find_element_by_xpath(
            '//span[@title=' + target + ']')
    except:
        pass

ac = ActionChains(driver)
ac.move_to_element(elem).click().perform()
time.sleep(2)

url = driver.page_source

def readMessage():
    threading.Timer(5.0, readMessage).start()
    url = driver.page_source
    soup = bs(url, "lxml")

    try:
        gotdiv = soup.find_all("div", { "class" : "msg msg-group" })[-1]
    except IndexError:
        gotdiv = 'null'

    if gotdiv == 'null':
        div = soup.find_all("div", { "class" : "bubble bubble-text copyable-text" })[-1]
        # print(div)
    else:
        div = soup.find_all("div", { "class" : "msg msg-group" })[-1]

    text = div.find_all('span')
    print(text)

    try:
        gottext = text[4].find_all(text=True)[1]
    except IndexError:
        gottext = 'null'

    if gottext == 'null':
        div = soup.find_all("div", { "class" : "chat-title" })[-1]
        name = div.find_all(text=True)[1]
        try:
            msg = text[-2].find_all(text=True)[1].lower()
        except IndexError:
            msg = "You replied last"
        time = text[-1].find(text=True)

    else: #group
        name = text[3].find_all(text=True)[1]
        try:
            msg = text[4].find_all(text=True)[1].lower()
        except IndexError:
            msg = "You replied last"
        try:
            time = text[-2].find(text=True)
        except:
            time = "None"


    print(name, msg, time)

# Getting appropriate reply from the csv
# Bot will lookup the csv for reply Only if the text contains the word buddy

if "buddy" in msg:

    with open('dict.csv', "r") as f:
        reader = csv.reader(f)
        chat = {}

        for row in reader:
            key = row[0]
            chat[key] = row[1:]
    try:
        gotreply = chat[msg]
    except KeyError:
        gotreply = 'null'

    print(gotreply)
