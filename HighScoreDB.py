import sqlite3


class HighScore:

    def __init__(self):
        self.db_name = 'HighScore.db'
        self.cursor = None
        self.table = None
        self.sqlite_table = None
        self.create_table()

    def connection(self):
        self.sqlite_table = sqlite3.Connection(self.db_name)
        self.cursor = self.sqlite_table.cursor()
        
    def create_table(self):
        self.connection()
        query = """
                CREATE TABLE IF NOT EXISTS HIGHSCORE (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                MAZESIZE INTEGER NOT NULL,
                SCORE FLOAT NOT NULL
                )
                """
        self.cursor.execute(query)
        self.sqlite_table.commit()
        self.sqlite_table.close()

    def insert_score(self,mazesize, score):
        self.connection()

        query = f"""
                INSERT INTO HIGHSCORE(MAZESIZE,SCORE)
                VALUES ({mazesize},{score})
                """
        self.cursor.execute(query)
        self.sqlite_table.commit()
        self.sqlite_table.close()

    def highest_score(self,mazesize):
        self.connection()

        query = f"""
                SELECT MIN(SCORE) FROM HIGHSCORE
                WHERE MAZESIZE IN ({mazesize})
                """
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.sqlite_table.close()
        return result[0]