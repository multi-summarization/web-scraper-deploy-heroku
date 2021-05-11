from psycopg2 import connect, Error
from os.path import join, dirname
import os


try:
    connection = connect(os.environ.get("DATABASE_URL"), 
                                user=os.environ.get("DB_USER"), 
                                password=os.environ.get("DB_PASSWORD"), 
                                host=os.environ.get("DB_HOST"))
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE articles (id SERIAL PRIMARY KEY, source VARCHAR, headline VARCHAR, link VARCHAR,category VARCHAR, content VARCHAR)")
    connection.commit()
    connection.close()
except Error as e:
    print(e)