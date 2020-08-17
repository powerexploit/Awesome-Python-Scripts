from app import Scrap

print('-----------------')
pub_name = input('Enter the comma seperated list of publication names(The Startup, Medium ...): ').split(',')
pub_link = input('Enter the comma seperated links of publications (https://medium.com/swlh, https://towardsdatascience.com  ...): ').split(',')

if len(pub_name) != len(pub_link):
    print('Please Enter links of all publications!')

pub_dict = {i: j for i, j in zip(pub_name, pub_link)}

choice = input("The default information passed is:\nNumber=5\nstart_date='2019-01-01'\nend_date='2019-08-01'\nyear=2019\n\nDo you want to change it? (Y/N): ")

if choice == 'Y':
    s_date = input("Enter new start date in format (YYYY-MM-DD): ")
    e_date = input("Enter new end date in format (YYYY-MM-DD): ")
    new_year = int(input("Enter year: "))
    num = int(input("Enter number of random samples: "))
else:
    s_date = '2019-01-01'
    e_date = '2019-08-01'
    new_year = 2020
    num = 5

print('Process started ...')
a = Scrap(urls_dict=pub_dict, number=num, start_date=s_date, end_date=e_date, year=new_year)
a.scrap()
a.dataframe().to_csv('results.csv')
print(a.dataframe())
print('-----------------')
print('Process ended... Thanks for using!')
