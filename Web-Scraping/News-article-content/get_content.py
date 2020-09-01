#Imports and dependencies
import nltk
nltk.download("punkt")
from newspaper import Article

URL = input("Enter the URL of the article ")
article = Article(URL)

#The content is processed
article.download()
article.parse()
article.nlp()

with open("article.txt" , "w") as f:
    f.write(article.text) 
