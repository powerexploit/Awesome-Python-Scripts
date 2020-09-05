# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class ZomatoScrapePipeline:

    def create_connection(self):
    # creates connection with the database(host_name,user_name,password,database_name)
        mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'zomato_scrape')  
        
        mycursor = mydb.cursor()
        
        return mydb,mycursor


    def insert_data(self,item):
        name = item['name'] 
        address = item['address'] 
        cost_per_two = item['cost_per_two'] 
        timings = item['timings'] 
        category = item['category']  
        cusine = item['cusine']  
        detailed_address = item['detailed_address'] 
        featured_in = item['featured_in']  
        discount = item['discount'] 
        try:
            mydb,mycursor = self.create_connection()
            
            
            mycursor.execute("INSERT INTO zomato_gandhinagar_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,address,cost_per_two,timings,category,cusine,detailed_address,featured_in,discount))
            mydb.commit()
        except Exception as e:
            print("Some exception occured in fetching data from databse {}".format(e))
        finally:
            try:
                mydb.close()
                mycursor.close()
            except Exception as e:
                print("Database connection already closed.")

    def process_item(self, item, spider):
        print("++++++++++++++++++++++++++++++++ i am in pipelines.py ++++++++++++++++++++++++++++++++++++++++++++++")
        print(item)
        self.insert_data(item)   
        print("+++++++++++++++++++++++++++++++++++ out now +++++++++++++++++++++++++++++++++++++++++++++++++++++++")
