from bs4 import BeautifulSoup

import requests

URL = input("ENTER PRODUCT URL: ")


req_data = requests.get(URL)
review_soup = BeautifulSoup(req_data.content, "html.parser")

base_url = "https://www.flipkart.com"
data = review_soup.find('div', {"class": "swINJg _3nrCtb"}).find_parent().get("href")

review_url = base_url + data
all_review_data = requests.get(review_url)
all_review_soup = BeautifulSoup(all_review_data.content, "html.parser")
review_url

all_reviews = review_soup.find_all('div', {'class': 'col _39LH-M'})
len(all_reviews)

header_list = []
detailed_review_list = []
user_list = []
rating_list = []
like_dislikes_list = []
count = 0
base_url = "https://www.flipkart.com"

while(count<11):
    
    print(review_url)
    all_review_data = requests.get(review_url)
    all_review_soup = BeautifulSoup(all_review_data.content, "html.parser")
    all_reviews = all_review_soup.find_all('div', {'class': 'ooJZfD _2oZ8XT col-9-12'})
    #print(all_reviews)   
    for review in all_reviews:
        header = review.find_all("p", {"class": "_2xg6Ul"})
        user = review.find_all("p", {"class": "_3LYOAd _3sxSiS"})
        detailed_review = review.find_all("div", {"class": "qwjRop"})
        rating = review.find_all("div", {"class": "hGSR34 E_uFuv"})
        likes_dislikes = review.find_all("span", {"class": "_1_BQL8"})

        header = [e.text for e in header]
        user = [e.text for e in user]
        detailed_review = [e.text for e in detailed_review]
        rating = [e.text for e in rating]
        likes_dislikes = [e.text for e in likes_dislikes]

        header_list.append(header)
        user_list.append(user)
        detailed_review_list.append(detailed_review)
        rating_list.append(rating)
        like_dislikes_list.append(likes_dislikes)

    count+=1
    review_url = base_url + all_review_soup.find_all("a", {"class": "_3fVaIS"})[-1].get("href")


user_list

base_url = "https://www.flipkart.com"
data = review_soup.find('div', {"class": "swINJg _3nrCtb"}).find_parent().get("href")

review_url = base_url + data
review_url



user_list = [item for sublist in user_list for item in sublist]
header_list = [item for sublist in header_list for item in sublist]
detailed_review_list = [item for sublist in detailed_review_list for item in sublist]
rating_list = [item for sublist in rating_list for item in sublist]
like_dislikes_list = [item for sublist in like_dislikes_list for item in sublist]

i=0
while(i<20):
    print(str(i+1) + ". " + user_list[i] + ":")
    print(rating_list[i] + " stars")
    print(header_list[i])
    print(detailed_review_list[i])
    print(like_dislikes_list[i])
    print("\n\n")
    i+=1
