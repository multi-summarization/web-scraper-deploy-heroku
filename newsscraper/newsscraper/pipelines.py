# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import psycopg2

class NewsscraperPipeline:
    """
    A pipeline to store scraped news articles to a database.
    """
    def __init__(self, sql_user, sql_password, sql_host, sql_port):
        self.sql_user = sql_user
        self.sql_password = sql_password
        self.sql_host = sql_host
        self.sql_port = sql_port


    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sql_user = settings['DB_USER'],
            sql_password = settings['DB_PASSWORD'],
            sql_host = settings['DB_HOST'],
            sql_port = settings['DB_PORT']
        )



    def open_spider(self, spider):
        self.connection = psycopg2.connect(database=settings['DB_NAME'], 
                               user=self.sql_user, 
                               password=self.sql_password, 
                               host=self.sql_host, 
                               port=self.sql_port)
        self.cursor = self.connection.cursor()
        #print("Database opened successfully")

    def close_spider(self, spider):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")




    def process_item(self, item, spider):
        return item
