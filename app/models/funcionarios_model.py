import sqlite3

class FuncionariosModel:
    def __init__(self, database='funcionarios.db'):
        self.db = database
        self.create_tables()
        
    def connect(self):
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()

    # CREATE    
    def create_tables(self):
        ...
        
    # WRITE (INSERT)
    
    # READ ALL (SELECT)

    # READ ONE (SELECT)
    
    # UPDATE
    
    # DELETE