import customtkinter as ctk



class AdmFuncView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        titulo_pagina = ctk.CTkLabel(self, text="ADM FUNCIONÁRIOS")
        titulo_pagina.pack()        

    # Treeview de estoque

    # Listar produtos e quantidades geral
    # Listar produtos e quantidades por lote

    # CRUD de estoque
    # Verificar detalhes de estoque