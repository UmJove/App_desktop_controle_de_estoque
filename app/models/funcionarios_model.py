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
        self.connect()
        self.cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS funcionario(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT NOT NULL,
                senha_login TEXT NOT NULL,
                nome TEXT NOT NULL,
                cargo TEXT NOT NULL,
                adm BOOLEAN
            )
        """
        )
        
    # WRITE (INSERT)
    def insert_funcionario(self, user_name, senha_login, nome, cargo, adm):
        self.connect()        
        
        self.cursor.execute(
            """
                INSERT INTO funcionario (
                    user_name,
                    senha_login,
                    nome, 
                    cargo,
                    adm) 
                VALUES (?, ?, ?, ?, ?)  
            """,
            (user_name, senha_login, nome, cargo, adm)
        )
        
        self.conn.commit()
        self.conn.close()
    
    # READ ALL (SELECT)
    def listar_funcionarios(self):
        self.connect()
        self.cursor.execute("""SELECT * FROM funcionario""")
        produtos = self.cursor.fetchall()
        print(produtos)
        self.conn.commit()
        self.conn.close()  
    

    # READ ONE (SELECT)
    
    # UPDATE
    
    # DELETE
    
if __name__ == "__main__":
    database = FuncionariosModel()
    database.insert_funcionario("@adm", "ADMINIT", "adm0", "adm", True)
    database.listar_funcionarios()