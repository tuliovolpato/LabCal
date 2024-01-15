import pymysql

class BancoDeDados:
    def __init__(self, host, user, password, database):
        self.dbConnection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
