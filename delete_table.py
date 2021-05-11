from psycopg2 import connect, Error
import os
from os.path import join, dirname

try:
    connection = connect(database=os.environ.get("DB_NAME"), 
                                user=os.environ.get("DB_USER"), 
                                password=os.environ.get("DB_PASSWORD"), 
                                host=os.environ.get("DB_HOST"))
    cursor = connection.cursor()
    cursor.execute("TRUNCATE TABLE articles")
    connection.commit()
    connection.close()
except Error as e:
    print(e)