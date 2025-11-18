import sqlite3

class FuncionariosModel:
    def __init__(self, database='funcionarios.db'):
        self.db = database
        self.create_tables()
        
    def connect(self):
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()

    # CREATE TABLE    
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
    def inserir_funcionario(self, user_name, senha_login, nome, cargo, adm):
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
        funcionarios = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()  
        return funcionarios

    # READ ONE (SELECT)
    def selecionar_funcionario(self, funcionario_id):
        self.connect()
        
        self.cursor.execute(
            """
                SELECT * FROM funcionario WHERE id = ?
            """, (funcionario_id)
        )
        funcionario_selecionado = self.cursor.fetchone()
        self.conn.commit()
        self.conn.close()
        return funcionario_selecionado       
    
    # UPDATE
    def atualizar_funcionario(self, funcionario_id, user_name, senha_login, nome, cargo, adm):
        self.connect()
        
        self.cursor.execute(
            """
                UPDATE funcionario SET 
                    user_name = ?,
                    senha_login = ?,
                    nome = ?,
                    cargo = ?,
                    adm = ?
                WHERE id = ?
            """, (user_name, senha_login, nome, cargo, adm, funcionario_id)
        )
        self.conn.commit()
        self.conn.close()
    
    # DELETE
    def excluir_funcionario(self, funcionario_id):
        self.connect()
        
        self.cursor.execute(
            """
                DELETE FROM funcionario WHERE id = ?
            """, (funcionario_id,)
        )

        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    func_db = FuncionariosModel()
    print("__\n\n")

    # func_db.inserir_funcionario("@mikael", "555", "Mikael", "Vendedor", False)
    # func_db.inserir_funcionario("@mariana", "555", "Mariana", "Florista", False)
    # print(func_db.listar_funcionarios())
    # print(func_db.selecionar_funcionario("1"))
    
    # for i in range(1, 6):
    #     print(func_db.selecionar_funcionario(str(i)))
    # # print("\n>>>>> UPDATE <<<<<")
    # # func_db.atualizar_funcionario(3, "@joseph", "555", "Joseph", "Florista", False)
    # # for i in range(1, 6):
    #     print(func_db.selecionar_funcionario(str(i)))

    # for i in range(1, 6):
    #     print(func_db.selecionar_funcionario(str(i)))
    # print("\n>>>>> DELETE <<<<<")
    # func_db.excluir_funcionario(5)
    # for i in range(1, 6):
    #     print(func_db.selecionar_funcionario(str(i)))