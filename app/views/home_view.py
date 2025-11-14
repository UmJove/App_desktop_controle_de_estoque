import customtkinter as ctk

class HomeView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#0f1113")
        self.controller = controller