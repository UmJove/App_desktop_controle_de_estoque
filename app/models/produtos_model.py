import sqlite3

class ProdutosModel:
    def __init__(self, database='produtos.db'):
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
            CREATE TABLE IF NOT EXISTS produto(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                qtd_estoque INTEGER NOT NULL
                )
        """
        )
        
        self.cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS lote(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                produto_id INTEGER NOT NULL,
                qtd_lote INTEGER NOT NULL,
                fabricacao TEXT,
                validade TEXT,
                registro TEXT,
                FOREIGN KEY(produto_id) REFERENCES produto(id)
                )
        """
        )
        
        
        self.conn.commit()
        self.conn.close()
    
    # WRITE
    def insert_produto(self, nome, qtd_estoque):
        self.connect()        
        
        self.cursor.execute(
        """
            INSERT INTO produto (nome, qtd_estoque) VALUES (?, ?)  
        """,
        (nome, qtd_estoque)
        )
        
        self.conn.commit()
        self.conn.close()
    
    # READ ALL (LISTAR)
    def list_produtos(self):
        self.connect()
        
        self.cursor.execute(
            """
                SELECT * FROM produto
            """
        )
        produtos = self.cursor.fetchall()
        print(produtos)
        self.conn.commit()
        self.conn.close()    
    
    # READ ONE (SELECT) Incompleto
    # def select_produto(self, produto_id):
    #     self.connect()
        
    #     self.cursor.execute(
    #         """
    #             SELECT * FROM produto WHERE id = ?
    #         """
    #     )
    #     produtos = self.cursor.fetchall()
    #     print(produtos)
    #     self.conn.commit()
    #     self.conn.close()        
    
if __name__ == "__main__":
    database = ProdutosModel()
    # database.insert_produto("Balde", 10)
    database.listar_produtos()
        