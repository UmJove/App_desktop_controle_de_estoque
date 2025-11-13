import sqlite3

class Database:
    def __init__(self, database='funcionarios.db'):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        self.create_tables()
