import customtkinter as ctk

from app.models.funcionarios import FuncionariosModel
from app.models.produtos import ProdutosModel

from app.views.login_view import LoginView
from app.views.home_view import HomeView


class AppController:
    def __init__(self):
        self.funcionarios = FuncionariosModel()
        self.produtos = ProdutosModel()
        self.root = ctk.CTk()
        self.root.geometry("800x600")

        # Tela de login
        self.login_view = LoginView(self.root, self)
        self.login_view.pack(fill="both", expand=True)        
        
    def run(self):
        self.root.mainloop()
        


if __name__ == "__main__":
    app = AppController()
    app.run()
