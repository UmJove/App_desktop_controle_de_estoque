import customtkinter as ctk



class GerEstoqueView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        titulo_pagina = ctk.CTkLabel(self, text="GER ESTOQUE")
        titulo_pagina.pack()        

    # Cadastrar funcionário
    