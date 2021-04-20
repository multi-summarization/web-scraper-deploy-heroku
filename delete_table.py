from mysql.connector import connect, Error
import os


connection = connect(database=os.environ.get("DB_USER"), 
                               user=os.environ.get("DB_USER"), 
                               password=os.environ.get("DB_PASSWORD"), 
                               host=os.environ.get("DB_HOST"))
cursor = connection.cursor()
cursor.execute("TRUNCATE TABLE articles")
connection.commit()
connection.close()