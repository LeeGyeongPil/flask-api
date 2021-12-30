import pymysql, os
from dotenv import load_dotenv

load_dotenv()

class Database():
    def __init__(self):
        self.db = pymysql.connect(host=os.getenv('DB_HOST'),
                                  port=int(os.getenv('DB_PORT')),
                                  user=os.getenv('DB_USERNAME'),
                                  password=os.getenv('DB_PASSWORD'),
                                  db=os.getenv('DB_DATABASE'),
                                  charset='utf8mb4')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args) 
 
    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchone()
        return row
 
    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchall()
        return row
 
    def commit(self):
        self.db.commit()