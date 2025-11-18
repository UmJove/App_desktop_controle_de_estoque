
import customtkinter as ctk


class RgLoteView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.configure(fg_color="darkblue")
        titulo_pagina = ctk.CTkLabel(self, text="RG NOVO LOTE")
        titulo_pagina.pack()        