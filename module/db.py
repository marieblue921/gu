class Database():
    def __init__(self):
        self.db = pymysql.connect(
                host = 'localhost',
                user = 'root',
                password = 'Inno160401**',
                db = 'youth1004',
                charset='utf8',
                autocommit = True
                )
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeAll(self,query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def commit():
        self.db.commit()

