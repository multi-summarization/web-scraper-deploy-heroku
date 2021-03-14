# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from mysql.connector import connect, Error


class NewsscraperPipeline:
    """
    A pipeline to store scraped news articles to a database.
    """
    def __init__(self, sql_user, sql_password, sql_host, sql_db_name, sql_port):
        self.sql_user = sql_user
        self.sql_password = sql_password
        self.sql_host = sql_host
        self.sql_db_name = sql_db_name
        self.sql_port = sql_port


    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sql_user = crawler.settings.get('DB_USER'),
            sql_password = crawler.settings.get('DB_PASSWORD'),
            sql_host = crawler.settings.get('DB_HOST'),
            sql_db_name = crawler.settings.get('DB_NAME'),
            sql_port = crawler.settings.get('DB_PORT')
        )



    def open_spider(self, spider):
        self.connection = connect(database=self.sql_db_name, 
                               user=self.sql_user, 
                               password=self.sql_password, 
                               host=self.sql_host)
        self.cursor = self.connection.cursor()
        #print("Database opened successfully")

    def close_spider(self, spider):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("SQL connection is closed")




    def process_item(self, item, spider):
        #self.cursor.execute("CREATE TABLE articles (id INT AUTO_INCREMENT PRIMARY KEY, source VARCHAR(255), headline VARCHAR(255), link VARCHAR(255), content VARCHAR(2000))")
        
        cmd = "INSERT INTO articles (source, headline , link, content)  VALUES (%s, %s, %s, %s)"
        val = (item['source'], item['headline'], item['link'], item['content'])
        #uncomment the lines below to send data to database
        #self.cursor.execute(cmd, val)  
        #self.connection.commit()
        
        #self.cursor.execute("SELECT * FROM articles")
        #myresult = self.cursor.fetchall()
        #for x in myresult:
        #    print(x)
        
        return item

import json

from itemadapter import ItemAdapter

class JsonWriterPipeline:

    def open_spider(self, spider):
        self.file = open('items.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item
