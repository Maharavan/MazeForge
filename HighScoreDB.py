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
                DIFFICULTY TEXT,
                SCORE FLOAT NOT NULL
                )
                """
        self.cursor.execute(query)
        self.sqlite_table.commit()
        self.sqlite_table.close()

    def insert_score(self,difficulty, score):
        self.connection()

        query = f"""
                INSERT INTO HIGHSCORE(DIFFICULTY,SCORE)
                VALUES (?,?)
                """
        self.cursor.execute(query,(difficulty,score))
        self.sqlite_table.commit()
        self.sqlite_table.close()

    def highest_score(self,difficulty):
        self.connection()

        query = f"""
                SELECT MIN(SCORE) FROM HIGHSCORE
                WHERE DIFFICULTY IN (?)
                """
        self.cursor.execute(query,(difficulty,))
        result = self.cursor.fetchone()
        self.sqlite_table.close()
        return result[0]
    
    def retrieve_highest_score(self):
        self.connection()
        diff = {'easy':'0.00','medium':'0.00','hard':'0.00'}
        for mode in diff:
            res = self.highest_score(mode)
            diff[mode]= res if res!=None else diff[mode]
        return diff


