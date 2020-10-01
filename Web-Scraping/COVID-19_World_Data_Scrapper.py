# Importing the necessary libraries to scrap and store data in excel format

import pandas as pd
#supress warnings
import warnings
warnings.filterwarnings('ignore')
import requests
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"



def get_all_tables(soup):
    """Extracts and returns all tables in a soup object"""
    return soup.find_all("table")

def get_table_headers(table):
    """Given a table soup, returns all the headers"""
    headers = []
    for th in table.find("tr").find_all("th"):
        headers.append(th.text.strip())
    return headers


def get_table_rows(table):
    """Given a table, returns all its rows"""
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = []
        # grab all td tags in this table row
        tds = tr.find_all("td")
        if len(tds) == 0:
            # if no td tags, search for th tags
            # can be found especially in wikipedia tables below the table
            ths = tr.find_all("th")
            for th in ths:
                cells.append(th.text.strip())
        else:
            # use regular td tags
            for td in tds:
                cells.append(td.text.strip())
        rows.append(cells)
    return rows

def save_as_csv(table_name, headers, rows):
    pd.DataFrame(rows, columns=headers).to_csv(f"{table_name}.csv")
    
    
def main(URL):    
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    # extract all the tables from the web page
    tables = get_all_tables(soup)
    print(f"[+] Found a total of {len(tables)} tables.")
    # iterate over all tables
    for itr, table in enumerate(tables, start=1):
        # get the table headers
        headers = get_table_headers(table)
        # get all the rows of the table
        rows = get_table_rows(table)
        # save table as csv file
        table_name = f"table-{itr}"
        if itr==1:
            print(f"[+] Saving {table_name}")
            save_as_csv(table_name, headers, rows)
            break
        
if __name__ == "__main__":
    import sys
    try:
        URL = 'https://www.worldometers.info/coronavirus/'
    except IndexError:
        exit(1)
    main(URL)


"""
To see Output:

df = pd.read_csv('table-1.csv')
df = df[8:223]
df.head()

"""
