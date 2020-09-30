import tabula
import pandas as pd
import sys

def extract(path, number_pages):
    tables = tabula.read_pdf(path, multiple_tables=True, pages=number_pages)
    count = 1
    if len(tables)!=0:
        for table in tables:
            print
            print(f"Saving file -{count}")
            table.to_csv(f'Table- {count}.csv')
            count += 1
        print("All tables saved as seperate files !")
    else:
        print("No tables found !")

if __name__ == "__main__":
    extract(sys.argv[1], sys.argv[2])