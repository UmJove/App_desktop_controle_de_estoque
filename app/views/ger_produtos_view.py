import customtkinter as ctk



class GerProdView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        titulo_pagina = ctk.CTkLabel(self, text="GER PRODUTOS")
        titulo_pagina.pack()        

    # Adicionar novo produto
    # Editar produtos
    # Excluir produtos
    # CRUD Produtos
