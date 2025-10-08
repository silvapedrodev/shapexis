import sqlite3


class DBProxy:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS scores (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        avatar TEXT NOT NULL,
                        score INTEGER NOT NULL,
                        date TEXT NOT NULL
                    )
                ''')

    def save_score(self, data):
        self.connection.execute(
            '''
            INSERT INTO scores (name, avatar, score, date)
            VALUES (:name, :avatar, :score, :date)
            ''',
            data
        )
        self.connection.commit()

    def retrieve_top10(self) -> list:
        return self.connection.execute(
            '''
            SELECT * FROM scores
            ORDER BY score DESC
            LIMIT 10
            '''
        ).fetchall()

    def close(self):
        self.connection.close()
