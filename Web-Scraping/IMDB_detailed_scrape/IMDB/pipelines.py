# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class ImdbPipeline:

    def create_connection(self):
    # creates connection with the database(host_name,user_name,password,database_name)
        mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'IMDB_scrape')  
        
        mycursor = mydb.cursor()
        
        return mydb,mycursor


    def insert_data(self,item):
        
        movie_name = item['movie_name']
        movie_year = item['movie_year'] 
        category = item['category']
        
        try:
            mydb,mycursor = self.create_connection()
            mycursor.execute('INSERT INTO movies_data VALUES (%s,%s,%s)',(movie_name,movie_year,category))
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
        print("+++++++++++++++++++++++++++++++++++")
