import sqlite3

class ProdutosModel:
    def __init__(self, database='produtos.db'):
        self.db = database
        self.create_tables()
    
    def connect(self):
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
    # C(W)RUD
    # CREATE TABLE (produto e lote)
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
                    fabricacao TEXT NOT NULL,
                    validade TEXT NOT NULL,
                    registro TEXT NOT NULL,
                    responsavel TEXT NOT NULL,
                    FOREIGN KEY(produto_id) REFERENCES produto(id)
                    )
            """
        )
        
        
        self.conn.commit()
        self.conn.close()
    
    # WRITE (INSERT) - produto
    def inserir_produto(self, nome, qtd_estoque):
        self.connect()        
        
        self.cursor.execute(
            """
                INSERT INTO produto (nome, qtd_estoque) VALUES (?, ?)  
            """,
            (nome, qtd_estoque)
        )
        self.conn.commit()
        self.conn.close()
        print('produto cadastrado')

    # WRITE (INSERT) - lote
    def inserir_lote(self, produto_id: int, qtd_lote: int, fabricacao:str, validade:str, registro:str, responsavel:str):
        self.connect()        
        
        self.cursor.execute(
            """
                INSERT INTO lote (produto_id, 
                                     qtd_lote, 
                                     fabricacao,
                                     validade,
                                     registro,
                                     responsavel) 
                                     VALUES (?, ?, ?, ?, ?, ?)  
            """,
            (produto_id, qtd_lote, fabricacao, validade, registro, responsavel)
        )
        
        self.conn.commit()
        self.conn.close()
    
    # READ ALL (SELECT) - produto
    def listar_produtos(self):
        self.connect()
        
        self.cursor.execute(
            """
                SELECT * FROM produto
            """
        )
        produtos = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        return produtos    
    
    # READ ALL (SELECT) - lote
    def listar_lotes(self):
        self.connect()
        
        self.cursor.execute(
            """
                SELECT * FROM lote
            """
        )
        lotes = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        return lotes    
    
    # READ ONE (SELECT) - produto
    def selecionar_produto(self, produto_id):
        self.connect()
        
        self.cursor.execute(
            """
                SELECT * FROM produto WHERE id = ?
            """, (produto_id)
        )
        produto_selecionado = self.cursor.fetchone()
        self.conn.commit()
        self.conn.close()
        return produto_selecionado        
    
    # READ ONE (SELECT) - lote
    def selecionar_lote(self, lote_id):
        self.connect()
        
        self.cursor.execute(
            """
                SELECT * FROM lote WHERE id = ?
            """, (lote_id)
        )
        lote_selecionado = self.cursor.fetchone()
        self.conn.commit()
        self.conn.close()
        return lote_selecionado        
    
    # UPDATE - produto
    def atualizar_produto(self, produto_id, novo_nome, nova_qtd_estoque):
        self.connect()
        
        self.cursor.execute(
            """
                UPDATE produto SET 
                    nome = ?,
                    qtd_estoque = ?
                WHERE id = ?
            """, (novo_nome, nova_qtd_estoque, produto_id)
        )
        self.conn.commit()
        self.conn.close()

    # UPDATE - lote
    def atualizar_lote(self, lote_id:int, produto_id: int, qtd_lote: int, fabricacao:str, validade:str, registro:str, responsavel:str):
        self.connect()
        
        self.cursor.execute(
            """
                UPDATE lote SET 
                    produto_id = ?,
                    qtd_lote = ?,
                    fabricacao = ?,
                    validade = ?,
                    registro = ?,
                    responsavel = ?
                WHERE id = ?
            """, (produto_id, qtd_lote, fabricacao, validade, registro, responsavel, lote_id)
        )
        self.conn.commit()
        self.conn.close()

    # DELETE - produto
    def excluir_produto(self, produto_id):
        self.connect()
        
        self.cursor.execute(
            """
                DELETE FROM produto WHERE id = ?
            """, (produto_id,)
        )

        self.conn.commit()
        self.conn.close()

    # DELETE - lote
    def excluir_lote(self, lote_id):
        self.connect()
        
        self.cursor.execute(
            """
                DELETE FROM lote WHERE id = ?
            """, (lote_id,)
        )

        self.conn.commit()
        self.conn.close()

    
if __name__ == "__main__":
    database = ProdutosModel()
    print("__\n\n")

    # TESTES - CRUD DE PRODUTO

    database.inserir_produto("Vaso", 10)
    database.inserir_produto("Rosa branca", 15)
    database.inserir_produto("Rosa Amarela", 42)

    # print("LISTA DE PRODUTOS")
    # print(database.listar_produtos())    
    # print("PRODUTO 3")
    # print("\n>>>>> UPDATE <<<<<")
    # database.atualizar_produto(3, "Rosa Amarela", 42)
    # print("PRODUTO 3")
    # print(database.selecionar_produto("3"))
    
    # print(database.selecionar_produto("1"))
    # print("\n >>>> DELETE <<<<")
    # database.excluir_produto("1")
    # print(database.selecionar_produto("1"))
    
    # database.excluir_produto("5")   
    # print(database.listar_produtos())    
    # for i in range(9, 19):
    #     indice_em_str = str(i)
    # print(database.listar_produtos())    


    # TESTES - CRUD DE LOTE

    # database.inserir_lote(5, 10, "2025-10-15", "2025-20-25", "2025-10-16", "Marina")
    # database.inserir_lote(5, 10, "2025-10-15", "2025-20-25", "2025-10-16", "Anna")
    # # print("\nLOTE 3")
    # print(database.selecionar_lote("3"))
    # # print("\n>>>>> UPDATE <<<<<")
    # database.atualizar_lote(4, 3, 69, "2025-10-17", "2025-10-27", "2025-10-20", "Giullyannah")
    # print("\nLOTE 3")
    # print(database.selecionar_lote("3"))
    # print(database.listar_lotes())

    # for i in range(9):
    #     print(database.selecionar_lote(str(i)))
    # print("\n>>>> DELETE <<<<\n")
    # database.excluir_lote("5")
    # for i in range(9):
    #     print(database.selecionar_lote(str(i)))
    
    