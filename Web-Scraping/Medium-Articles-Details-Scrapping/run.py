from app import Scrap


a = Scrap(urls_dict={"Towards Data Science": "https://towardsdatascience.com",
                     "The Startup":"https://medium.com/swlh",
                     }, number=50,
                     start_date='2019-01-01', end_date='2019-08-01',year=2019)
a.scrap()
a.dataframe().to_csv('results.csv')
print(a.dataframe())
