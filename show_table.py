from psycopg2 import connect
import os
from os.path import join, dirname


connection = connect(database=os.environ.get("DB_NAME"), 
                               user=os.environ.get("DB_USER"), 
                               password=os.environ.get("DB_PASSWORD"), 
                               host=os.environ.get("DB_HOST"))
cursor = connection.cursor()
cursor.execute("SELECT * FROM articles")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
connection.commit()
connection.close()