import mysql.connector
from urllib.parse import urlparse

class CategoryStorager:
    def __init__(self):
        pass

    def connect(self):
        url = urlparse('mysql://irasutoya_user:Irasutoya@20190901@localhost:3306/irasutoya')
        self.conn = mysql.connector.connect(
            host = url.hostname or 'localhost',
            port = url.port or 3306,
            user = url.username or 'root',
            password = url.password or 'password',
            database = url.path[1:] or 'test_database',
        )
        self.conn.ping(reconnect=True)
    

    def disconnect(self):
        self.conn.close()

    def insert(self, labels, links):
        cur = self.conn.cursor()
        records = []
        for record in zip(labels, links):
            records.append(record)
        cur.executemany("INSERT INTO `category` (`label`, `link`) VALUES (%s, %s)", records)
        self.conn.commit()
        cur.close()
    
    def selectAll(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM `category`")
        records = cur.fetchall()
        cur.close()
        return records