## USE: As a part of projects where you are required to do sentiment analysis on customer reviews data. </br>

Scrapy is a web crawling framework for a developer to write code to create, which defines how a particular site (or a group of websites) will be scrapped.

### Steps:</br>

1) From the conda-forge, install scrapy: </br>
>> conda install -c conda-forge scrapy

In case you want to install from system, use: 
>> pip install scrapy

2) Start a project:</br>
>> scrapy startproject amazon_reviews_scraping

3) A spider is a chunk of python code that determines how a web page will be scrapped, it's the main component that crwals the webpage and extracts contents from it.</br>
So copy your link from the product review you want to scrape, and run the following: </br>
>> scrapy genspider amazon_review <your-link-here>

4) Now you'll need to define a scrapy parser, which I've already done in: </br>
amazon_reviews_scraping/spider/scraper.py

5) Run the following to store the result in a csv file titled "reviews.csv", or you may change the name as per your convenience! </br>
>> scrapy runspider amazon_reviews_scraping/amazon_reviews_scraping/spiders/amazon_reviews.py -o reviews.csv
