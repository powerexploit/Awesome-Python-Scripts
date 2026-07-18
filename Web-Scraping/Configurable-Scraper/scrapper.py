import requests
from bs4 import BeautifulSoup
import json

# Load config
with open("config.json") as f:
    config = json.load(f)

url = config["url"]
tag = config["tag"]
class_name = config["class"]

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

elements = soup.find_all(tag, class_=class_name)

print(f"\nScraping from: {url}\n")

for i, el in enumerate(elements, 1):
    print(f"{i}. {el.text.strip()}")