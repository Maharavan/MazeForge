import sqlite3


class HighScore:

    def __init__(self):
        self.db_name = 'HighScore.db'
        self.cursor = None
        self.table = None

    def connection(self):
        sqlite_table = sqlite3.connection(self.db_name)
        self.cursor = sqlite_table.cursor()
        
    def create_table(self):
        self.connection()
        query = """
                CREATE TABLE IF NOT EXIST HIGHSCORE (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                SCORE INTEGER NOT NULL
                )
                """
        self.cursor.execute(query)
        self.sqlite_table.commit()

    def insert_score(self,score):
        self.connection()

        query = f"""
                INSERT INTO HIGHSCORE(SCORE)
                VALUES ({score})
                """
        self.cursor.execute(query)
        self.sqlite_table.commit()
