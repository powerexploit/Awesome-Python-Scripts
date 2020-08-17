# Medium-Articles-Details-Scrapping
This script will scrap details about medium articles published in a date range in the given publication. The dates are choosen randomly. If there is no article on that date, then that date is skipped. The results returned is a dataframe which can be saved in any format, currently saves as CSV.

# Requirements
- numpy
- pandas
- bs4
- requests

# How to run?
- Run the command: python run.py

# About the Scrap class
    A Scrapper to get details about medium articles published in a date range in a Publication by selecting random dates.

    Attributes
    ----------
    urls_dict : dict
        key-value pairs of the publication name with link. Example:
        urls_dict={"The Startup":"https://medium.com/swlh"}

    start_date : str
        starting date of the search. Default: 2020-01-01

    end_date : str
        ending date of the search. Default: 2020-08-01

    year : int
        year in which search has to be done. Default: 2020

    number: int
        number of random dates you want to pick. Default: 10

    Methods
    -------
    scrap():
        Scrapping process will be initiated by this method.

    dataframe():
        Returns the dataframe object.

