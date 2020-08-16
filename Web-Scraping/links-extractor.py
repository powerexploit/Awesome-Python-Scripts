# Importing required libraries
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from xlwt import Workbook 
from datetime import datetime

#Tacking URL input from user
url=input("Enter site to get links\n")
links=[]
while(len(url)==0):
    url=input("Enter site to get links\n")
try:
    # Sending request to server using Urllib
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_data = urlopen(req).read()

    #Beautyfying all data to html form 
    soup=BeautifulSoup(html_data,'html.parser')

    #Retriving all anchor tags in html data
    tags=soup('a')

    #Adding all href attribute values to list
    for tag in tags:
            if tag.has_attr('href'):
                links.append(tag['href'])
except:
    #Check if any errors
    print("Please check the URL properly")
if(len(links)==0):
    print("No links to fetch")
else:
    # Tackning workbook
    wb=Workbook()

    #Creaing sheet in workbook
    sheet1 = wb.add_sheet('Links')

    #adding all data in list to excel sheet
    for i in range(0,len(links)):
        sheet1.write(i,0,links[i])
    
    #Getting date and time to create file
    data_time=datetime.now()
    current_time = str(data_time.strftime("%H-%M-%S"))
    
    #Adding time to file name and saving file locally
    wb.save('links for '+current_time+'.xls')
    print("Done writing data to excel sheet")